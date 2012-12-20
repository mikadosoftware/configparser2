Trivial fix for ConfigParser
============================

Quick usage
-----------
::

    p = ConfigParser2.SafeConfigParser()
    p.read(filepath)
    print p.comment_store
    {'coffee::global': ['## Section dealing with my addictions\n'],   
     'coffee::espresso': ['## When in Rome, drink as the Romans drink\n'], 
     'coffee::latte': ['## my default cuppa\n']}


    print p.ini_as_rst()

    .. rst version of ini file


    coffee
    ------
    :espresso: ## When in Rome, drink as the Romans drink
    :global: ## Section dealing with my addictions
    :latte: ## my default cuppa


    Simple helper script:
  
    python docFromIni.py <my/ini/file> > docs/ini.rst

    
   

I often use .ini style files::

   [coffee]
   latte:with_caramel
   espresso:sixsugarsplease

But they always need explanatory text - and the *best* place 
to document a ini file is in the ini file::


   [coffee]
   ## Section dealing with my addictions

   latte:with_caramel 
   ## my default cuppa

   espresso:sixsugarsplease
   ## When in Rome, drink as the Romans drink


But ConfigParser just drops this stuff on the floor.
I would like my Sphinx maker to produce me a nice looking 
ini file document that is really easy to keep up.::

    coffee
    ------
    :section: Section dealing with my addictions

    :latte:  my default cuppa
  
    :espresso: When in Rome, drink as the Romans drink
  



Should look like this


coffee
------
:section: Section dealing with my addictions

:latte:  my default cuppa

:espresso: When in Rome, drink as the Romans drink

