Small app to collect the words and generate wordlist for different Indian languages.

Currently starting with Devanagari Script, Marathi language.


Requirement
===========

Python 3.15.

Install the dependencies into a virtualenv:

    python3.15 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt

The requirements are:

- Django 6.1 (the webapp, shabdakosh). scripts/update_words.py uses it too.
- django-tastypie (the read-only API under /api/).
- SQLAlchemy (only needed for scripts/shabda.py).
- psycopg2-binary (PostgreSQL driver).


Creating DB
====================

postgres
--------

CREATE DATABASE shabdakosh WITH ENCODING 'UTF8' TEMPLATE template0;

Then fill in the DATABASES settings in shabdakosh/settings.py and run:

    python -m shabdakosh.manage migrate --run-syncdb

(Run from the repository root.)

Useful links
============

http://dumps.wikimedia.org/backup-index.html (choose approriate language)

For marathi words:
http://code.google.com/p/tukaram/
