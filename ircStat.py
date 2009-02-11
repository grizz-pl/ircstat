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
	about = "______________\n" + __project__ + " ver. " + __version__ + " by " + __author__ + "\n\n" \
					+ "==> Source directory: " + sourceDir + "\n" \
					+ "==> Destination directory: " + destDir + "\n"
	return about

def verbose (msg):
	try:
		if sys.argv[1] == "-v":
			print msg;
	except IndexError:
		pass

def help():
	print about()
	try:
		if sys.argv[1] == "--help":
			print "OPTIONS:\n" \
							+ "--help\t Print this information\n" \
							+ "-v\t Be verbose\n"
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

def base():
	"""base loop"""
	verbose(about())
	#sourceDir = getSourceDir()
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
	print "DUPA!"
def main ():
	try:
		if sys.argv[1] == "--help":
			help()
		else:
			base() # if there is argv but differ than --help
	except IndexError:
		base() # if here is no argv

    
main() # run main loop
