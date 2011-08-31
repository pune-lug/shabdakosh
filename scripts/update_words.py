#!/opt/local/bin/python

import codecs
import re
import sys
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'shabdakosh.settings'
sys.path.append('_path_of_parent_dir_of_django_app_')

devnagari_chrs = ''.join(
    {unichr(x) for x in range(0x900, 0x980)} - \
    {unichr(x) for x in range(0x964, 0x970)}
)
other_chrs = ':,./<>?;"[]{}|-=_+!@#$%^&*()`~\'\\'
from shabdakosh.devanagari.models import shabda

f = codecs.open(sys.argv[1], encoding='utf-8')


def store_db(word=None):
    try:
        s = shabda.objects.get(shabda=word)
        s.kiti_vela += 1
    except:
        s = shabda()
        s.shabda = word
        s.kiti_vela = 1
    s.save()


def get_words(line=None):
    retval = []
    for w in re.split(r'[%s]' % (other_chrs), line, re.U):
        s = re.search(r'[%s]+' % (devnagari_chrs), w, re.U)
        if s:
            retval.append(s.group())
    return retval

skip = 0
i = skip
tot_words = 0
for l in f:
    if skip:
        skip -= 1
        print skip
        continue
    words = get_words(l)
    for w in words:
        store_db(w)
        print w.encode('utf-8')
        tot_words += 1
    i += 1
    print i, tot_words
