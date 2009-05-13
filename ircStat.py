#!/usr/bin/env python
# -*- coding: utf-8 -*-
#ircStat ver. 0.2 by grizz - Witek Firlej http://grizz.pl

__project__      = "ircStat"
__author__    = "Witold Firlej (http://grizz.pl)"
__version__   = "0.2"
__license__   = "GPL"
__copyright__ = "Witold Firlej"

import os,sys
# ====== some globals =============
sourceDir = "/home/users/grizz/Programowanie/Python/Projekty/ircStat/FreeNode/#olympusclub/" # Working directory
destDir = "/home/users/grizz/temp/"
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
        sourceDir = sys.argv[1] # get sourseDir from argv
    except IndexError:
        sourceDir = "." # if there is no argument, use current dir as sourceDir
    return sourceDir
"""
def generateGnuplotSettings(endDate):
	datafile = open("gnuplot.conf", "w")
	datafile.write("set encoding iso_8859_2\n")
	datafile.write("set title \"Aktywność #olympusclub\"\n")
	datafile.write("set xlabel \"Data\"\n")
	datafile.write("set ylabel \"Ilość wiadomości\"\n")
	datafile.write("set grid\n")
	datafile.write("set xdata time\n")
	datafile.write("set timefmt \"%Y-%m-%d\"\n")
	datafile.write("set format x \"%y %b %d\"\n")
	datafile.write("set terminal png small size 6000,800\n")
	datafile.write("set output \'wykres.png\'\n")
	datafile.write("plot [\"2008-05-11\" : \"" +endDate+"\"] \"data.dat\" using 1:2 with linespoints, \"average.dat\" using 1:2 with linespoints\n")
	datafile.close()

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
	verbose("==> calculating moving average")
	movingAverage()
	verbose("==> Generating gnuplot configuration file...")
	generateGnuplotSettings(record[:10]) # call function with last record, without number of lines, as endDate 
	verbose("==> Run gnuplot...")
	os.system("iconv -c -f UTF-8 gnuplot.conf -t iso-8859-2 -o gnuplot.confISO") #necessary for polish letters
	os.system("gnuplot -persist gnuplot.confISO")
	verbose("==> Copy graph to " + destDir)
	os.system("cp wykres.png " + destDir)
	verbose("ALL IS DONE!")

def movingAverage():
	numberoflines = []
	movingaverage = []
	dates = []
	averagedatafile = open("average.dat", "w")
	data = open("data.dat", "r")

	for line in data:
		dates.append(line.split()[0])
		numberoflines.append(int(line.split()[1]))

	rng = 0
	for number in numberoflines:
		start = rng
		stop = rng+30
		rng +=1
		suma = sum(numberoflines[start:stop])
		movingaverage.append(suma/30)

	for rng in range(len(open("data.dat", "rU").readlines())):
		record = str(dates[rng]) + " " + str(movingaverage[rng])
		verbose("==> Average: " + record)
		averagedatafile.write(record + "\n")

def main ():
	try:
		if sys.argv[1] == "--help":
			help()
		else:
			base() # if there is argv but differ than --help
	except IndexError:
		base() # if here is no argv

    
main() # run main loop
