import sys
import ConfigParser2


def run(inipath):
    """ """
    p = ConfigParser2.SafeConfigParser()
    p.read(inipath)
    return p.ini_as_rst()

if __name__ == '__main__':
    f = sys.argv[1:][0]
    print run(f)

