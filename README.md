Small app to collect the words and generate wordlist for different Indian languages.

Currently starting with Devanagari Script, Marathi language.


Requirement
===========

Mandatory
---------
Python 2.7.x. You may be able to get it working on 2.6.x.
(For 3.x, few modification may be required.)

Optional
--------

1. SQLAlchemy: If you use scripts/shabda.py, you will need SQLAlchemy.
   Python 3.x may be supported on this.

2. Django: If you want to use the webapp, shabdakosh, you will need
   django. scripts/update_words.py should be used in this case.


Creating DB
====================

postgres
--------

CREATE DATABASE shabdakosh WITH ENCODING 'UTF8' TEMPLATE template0;

Useful links
============

http://dumps.wikimedia.org/backup-index.html (choose approriate language)

For marathi words:
http://code.google.com/p/tukaram/
