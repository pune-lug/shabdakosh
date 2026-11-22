#!/usr/bin/env python3

import os
import re
import sys

# The directory above scripts/ holds the `shabdakosh` package; make it
# importable and initialise Django before importing any models.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shabdakosh.settings')

import django  # noqa: E402

django.setup()

from shabdakosh.devanagari.models import shabda  # noqa: E402

devnagari_chrs = ''.join(
    {chr(x) for x in range(0x900, 0x980)} - {chr(x) for x in range(0x964, 0x970)}
)
other_chrs = ':,./<>?;"[]{}|-=_+!@#$%^&*()`~\'\\'
other_re = re.compile('[%s]' % re.escape(other_chrs))

f = open(sys.argv[1], encoding='utf-8')


def store_db(word=None):
    try:
        s = shabda.objects.get(shabda=word)
        s.kiti_vela += 1
    except shabda.DoesNotExist:
        s = shabda()
        s.shabda = word
        s.kiti_vela = 1
    s.save()


def get_words(line=None):
    retval = []
    for w in other_re.split(line):
        s = re.search(r'[%s]+' % devnagari_chrs, w)
        if s:
            retval.append(s.group())
    return retval


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
        store_db(w)
        print(w)
        tot_words += 1
    i += 1
    print(i, tot_words)
