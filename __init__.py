# PyQtRibbon 0.0.1
# By RoadrunnerWMC
# Requires Python 3 and PyQt5
# Licensed under LGPL
# Basic documentation can be found by running this
# and calling documentation()




# Imports
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
Qt = QtCore.Qt




# Basic library things
def version():
    """Returns the PyQtRibbon version number"""
    ver = '0.0.1'
    return ver

def documentation():
    """Returns the PyQtRibbon help documentation"""
    doclist = ''

    doclist += 'PyQtRibbon %d by RoadrunnerWMC' % version()
    doclist += 'Help Documentation'
    doclist += '------------------'
    doclist += 'Docs will go here eventually.'
    doclist += ''
    doclist += ''
    doclist += ''
    doclist += ''

    docs = '\n'.join(doclist)
    return docs
