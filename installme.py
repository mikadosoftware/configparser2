
"""
trivial install script -

Will find current location of ConfigParser module,
and move the script named "ConfigParser2.py" in _this_ dir
to that location.

(basically shove the ConfigParser2 script into /usr/local/lib/python2.7)

"""

import os, shutil
import inspect
import ConfigParser

path_to_currentCP = inspect.getsourcefile(ConfigParser)
#ie '/usr/local/lib/python2.7/ConfigParser.py'
tgtdir = os.path.dirname(path_to_currentCP)
#ie '/usr/local/lib/python2.7'
curr_loc = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) 
src_file = os.path.join(curr_loc, "ConfigParser2.py")
tgt_file = os.path.join(tgtdir, "ConfigParser2.py")
shutil.copyfile(src_file, tgt_file)


