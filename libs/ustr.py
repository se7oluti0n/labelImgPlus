import sys



try:
    QString = unicode
except NameError:
    # Python 3
    QString = str

def ustr(x):
    '''py2/py3 unicode helper'''

    if sys.version_info < (3, 0, 0):
        if type(x) == str:
            return x.decode('utf-8')
        if type(x) == QString:
            return str(x)
        return x
    else:
        return x # py3
