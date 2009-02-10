#!/usr/bin/env python
# -*- coding: utf-8 -*-
#ircStat ver. 0.1 by grizz - Witek Firlej http://grizz.pl

__project__      = "ircStat"
__author__    = "Witold Firlej (http://grizz.pl)"
__version__   = "0.1"
__license__   = "GPL"
__copyright__ = "Witold Firlej"

import os,sys
# ====== some globals =============
destDir = "/home/users/grizz/Programowanie/Python/Projekty/ircStat/FreeNode/#olympusclub/" # Working directory
# ====== some globals END =============

def about ():
    """About ircStat"""
    print "______________"
    print __project__ + " ver. " + __version__ + " by " + __author__
    print ""

def verbose (msg):
    try:
        if sys.argv[1] == "-v":
            print msg;
    except IndexError:
         pass
    
""" TO DO later
def getDestDir ():
    try: 
        destDir = sys.argv[1] #Przekazany argument sprawdzić czy ma shlasha na początku, jak nie ma to dodać aktualny katalog.
    except IndexError:
        destDir = "." # if there is no argument, use current dir as destDir
    return destDir
"""

def main():
    """main loop"""
    about()
    #destDir = getDestDir()
    verbose("Working directory: " + destDir)
    verbose("Data gathering...")
    files = [d for d in os.listdir(destDir)]
    verbose (files)
    count = -1
    datafile = open("data.dat", "w")
    for file in files:
        for count, wiersz in enumerate(open(destDir+file, 'rU')):
            pass
        count += 1
        record =  file[:-4] + " %i" % count # filename (without ".log") and number of lines in it.
        verbose(record)
        datafile.write(record + "\n")
    datafile.close()

    

main() # run main loop