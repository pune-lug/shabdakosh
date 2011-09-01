#!/opt/local/bin/python

import os
import sys
import codecs
import re
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



DATABASE_NAME = 'shabdakosh'
DATABASE_HOST = 'localhost'
DATABASE_USER = 'postgres'
DATABASE_PASS = None
DATABASE_PORT = 5432

engine = create_engine('postgres://%s:%s@%s:%d/%s' % (DATABASE_USER, DATABASE_PASS, DATABASE_HOST, DATABASE_PORT, DATABASE_NAME), echo=False)

table_name = sys.argv[1]
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

devnagari_chrs = ''.join({unichr(x) for x in range(0x900, 0x980)}-{unichr(x) for x in range(0x964,0x970)})
other_chrs = ':,./<>?;"[]{}|-=_+!@#$%^&*()`~\'\\'
digits = ''.join([unichr(x) for x in range(0x966, 0x970)])

f = codecs.open(sys.argv[2], encoding='utf-8')

def get_words(line=None):
    retval = []
    for w in re.split(r'[%s]' % other_chrs, line, re.U):
        a = re.search(r'[%s][%s]*' % (devnagari_chrs, devnagari_chrs), w, re.U)
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
tot_words = 0
for l in f:
    if skip:
        skip -= 1
        print(skip)
        continue
    words = get_words(l)
    for w in words:
        try:
            tot_words += store_db(w)
        except Exception as e:
            pass
    i += 1
print 'New words: %d' % tot_words
