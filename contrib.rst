
Contributing back to the Python world
=====================================

Weirdly, for someone who has used Python for so long, 
I have not contributed anything back to the Python 
development team(s).  A long time ago I tried to supply a 
patch to csv.py but it was a function no-one but me it seemed
wanted.

Now I am in a similar position (ConfigParser2) but I am going to 
record my trials and tribulations

The situation
-------------

I wanted to comment an .ini file and then easily output docs 
from that ini file (ie into sphinx).  The actual fix was 
pretty simple (at least so far) - I just patched my local 
ConfigParser.py and told it to grab the comment lines instead
of chucking them.

I have stuck that into https://github.com/lifeisstillgood/configparser2

It works for me.

Start
=====

Now I would like to follow Jesse Noller's advice and contribute 
something.

http://jessenoller.com/2011/05/05/on-contribution/
http://docs.python.org/devguide/

* Problem #1

This is kind of a known problem, but it really is a biggie.
Python 3.  You see I am still running 2.7.  So is, well, almost everyone.

http://py3ksupport.appspot.com/


* Problem 2

They have made changes since 2.7.  Looks like I am going to be supporting
divedrging branches.  This is actually part of Problem #1 and really indicates
that we still do have a huge elephant in the room
http://hg.python.org/cpython/file/7c717d423160/Lib/configparser.py


* Problem 3

Installation
I am also looking at fixes for doctest (xxx) 
And the installation and distribute nightmare is also a problem - I have no real 
insight here but it does need fixing.


Step 1
======

Get set up with latest code and compilation.
And don't break your system...

ConfigParser is unlikely to be under heavy development so tracking the HEAD 
will be simplest.


http://docs.python.org/devguide/setup.html


Future of python
----------------

http://lucumr.pocoo.org/2011/12/7/thoughts-on-python3/

All this gets me thinking about the future of Python - its not big on 
mobile, its not the default onWindows, its has a place in Unix world but that
big place is web development - and its under threat from javascript

"now is not the time" is a horrible phrase - and almost always wrong.
Do something is better than do nothing.  

