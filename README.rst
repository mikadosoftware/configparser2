Trivial fix for ConfigParser
============================

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
    * Section dealing with my addictions

    * latte
      my default cuppa

    * espresso
      When in Rome, drink as the Romans drink





