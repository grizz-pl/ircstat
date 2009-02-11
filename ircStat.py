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
sourceDir = "/home/users/grizz/Programowanie/Python/Projekty/ircStat/FreeNode/#olympusclub/" # Working directory
destDir = "/home/grizz/wwwcostam"
# ====== some globals END =============

def about ():
	"""About ircStat"""
	about = "______________\n" + __project__ + " ver. " + __version__ + " by " + __author__ + "\n" \
					+ "==> Source directory: " + sourceDir + "\n" \
					+ "==> Destination directory: " + destDir + "\n"
	return about

def verbose (msg):
	try:
		if sys.argv[1] == "-v":
			print msg;
	except IndexError:
		pass
    
""" TO DO later
def getSourceDir ():
    try: 
        sourceDir = sys.argv[1] #Przekazany argument sprawdzić czy ma shlasha na początku, jak nie ma to dodać aktualny katalog.
    except IndexError:
        sourceDir = "." # if there is no argument, use current dir as sourceDir
    return sourceDir
"""

def main():
	"""main loop"""
	verbose(about())
	verbose
	#sourceDir = getSourceDir()
	verbose("==> Working directory: " + sourceDir)
	verbose("==> Data gathering...")
	files = [d for d in os.listdir(sourceDir)]
	count = -1
	datafile = open("data.dat", "w")
	for file in files:
		for count, wiersz in enumerate(open(sourceDir+file, 'rU')):
			pass
		count += 1
		record =  file[:-4] + " %i" % count # filename (without ".log") and number of lines in it.
		verbose(record)
		datafile.write(record + "\n")
	datafile.close()
	verbose("==> Generating gnuplot configuration file...")
	verbose("==> Run gnuplot...")
	verbose("==> Copy graph to " + destDir)
	verbose("ALL IS DONE!")

main() # run main loop
