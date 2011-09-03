#!/opt/local/bin/python

import os
import sys
import codecs
import re
import argparse

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def parse_opts(data):
    parser = argparse.ArgumentParser()
    parser.add_argument('--db-host', default='localhost')
    parser.add_argument('--db-name', default='shabdakosh')
    parser.add_argument('--db-user', default='postgres')
    parser.add_argument('--db-passwd', default=None)
    parser.add_argument('--db-port', default=5432)
    parser.add_argument('--db-type', default='postgres')
    parser.add_argument('--table-name', default='marathi_devnagari')
    parser.add_argument('--input-file')
    return parser.parse_args(data)


args = parse_opts(sys.argv[1:])

engine = create_engine('%s://%s:%s@%s:%d/%s' % (args.db_type, args.db_user , args.db_passwd, args.db_host, args.db_port, args.db_name), echo=False)

table_name = args.table_name
Base = declarative_base()

class Sangraha(Base):
    __tablename__ = table_name
    id = Column(Integer, primary_key=True)
    shabda = Column('shabda', String(convert_unicode=True), unique=True)
    kiti_vela = Column('kiti_vela', Integer)
    def __init__(self, *largs, **kargs):
        self.shabda = kargs['shabda']
        if 'kiti_vela' in kargs: self.kiti_vela = kargs['kiti_vela']
        
    def __repr__(self):
        return 'Name: ' % (self.shabda)


Base.metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
session = Session()

devnagari_start_chrs =  ''.join(
    {unichr(x) for x in range(0x904, 0x93a) + range(0x958, 0x962)} | \
    {unichr(0x950)} 
)

devnagari_chrs = ''.join(
    {unichr(x) for x in range(0x900, 0x980)} - \
    {unichr(x) for x in range(0x964, 0x970)}
)


other_chrs = ':,./<>?;"[]{}|-=_+!@#$%^&*()`~\'\\'
digits = ''.join([unichr(x) for x in range(0x966, 0x970)])

f = codecs.open(args.input_file, encoding='utf-8')

def get_words(data=None):
    retval = []
    for line in data.split('\n'):
        for w in re.split(r'[%s]' % other_chrs, line, re.U):
            a = re.search(r'[%s][%s]*' % (devnagari_start_chrs, devnagari_chrs), w, re.U)
            if a: 
                retval.append(a.group())
        return retval


def store_db(word):
    #session.rollback()
    f = 0
    x = session.query(Sangraha).filter_by(shabda=word).first()

    if x:
        x.kiti_vela += 1 
        session.add(x)
    else:
        w = Sangraha(shabda=word.encode('utf-8'), kiti_vela=1)
        session.add(w)
        f = 1
    session.commit()
    return f



skip = 0
i = skip
old_words = 0
new_words = 0
for l in f:
    if skip:
        skip -= 1
        print(skip)
        continue
    words = get_words(l)
    for w in words:
        try:
            if store_db(w):
                new_words += 1
            else:
                old_words += 1
        except Exception as e:
            pass
    i += 1

print 'Old words: %d' % old_words
print 'New words: %d' % new_words
