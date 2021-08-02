#!/usr/bin/env python


from datetime import datetime
import argparse
import time
import sys
import os


# Author MD Harrington  facebook https://www.facebook.com/mark.harrington.142892 links to this there as well for you
# code that prinst a text file to console  with colous set on chars in slow motion type writer effect 
# usage ::  python.py <yourfile.txt> 
# global colour settings 
# python version Python 2.7.14


CBLACK  = '\33[30m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE  = '\33[36m'
CWHITE  = '\33[37m'
CYAN  = '\033[1;36m'

CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'
CGREENBG  = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG   = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG  = '\33[46m'
CWHITEBG  = '\33[47m'

CGREY    = '\33[90m'
CRED2    = '\33[91m'
CGREEN2  = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2   = '\33[94m'
CVIOLET2 = '\33[95m'
CBEIGE2  = '\33[96m'
CWHITE2  = '\33[97m'

CGREYBG    = '\33[100m'
CREDBG2    = '\33[101m'
CGREENBG2  = '\33[102m'
CYELLOWBG2 = '\33[103m'
CBLUEBG2   = '\33[104m'
CVIOLETBG2 = '\33[105m'
CBEIGEBG2  = '\33[106m'
CWHITEBG2  = '\33[107m'
ENDC = '\033[0m'

 
arraylength=0 

# function  definitions


def f_clearscreen(time_delay):
	os.system('clear')
	time.sleep(time_delay) 
	for x in range(2):
		print('')
	
	


def f_openfile(fileopen):
	
	global paragraphs
	global arraylength
	
	# open the file 
	f = open(fileopen, "r")
	# read the open file 
	data =f.read()
	# split this into paragrapghs 
	paragraphs = data.split("\n\n")
	paragraphs[:] = (value for value in paragraphs if value != '\t')
	#get number of paragraghs 
	arraylength = len(paragraphs)
	# sleep 3
	
	time.sleep(4)
	# clear the screen
	os.system('clear')
	
	
		
	f.close()
	
def  readpar_lines(counter):
	 # make this global so that functions can see this
	global lines
	lines= paragraphs[counter].splitlines() 
	


def slowPrint():
	
	for line in lines:
		for mychar in line:
			sys.stdout.write(CWHITE + mychar)
			sys.stdout.flush()
			time.sleep(0.05)
	sys.stdout.write(ENDC)
	sys.stdout.flush()
	
	


def slowPrintMsgString(var):
	
	for mychar in var:
		sys.stdout.write(CBLUE + str(mychar))
		sys.stdout.flush()
		time.sleep(0.05)
	sys.stdout.write(ENDC)
	sys.stdout.flush()
	
# main execution starts here 

print("Ready")
f_clearscreen(4.00)

# get filename 
m_file = "instructions.txt"

# Print introduction 

slowPrintMsgString("Good evening all todays tutorial is on how to use git from within QT\n\n")
sys.stdout.flush() 

# open this file and split into paragraphs
f_openfile(m_file) 

# get user input and count 
for x in range(arraylength):
	# split each paragraph into lines
	readpar_lines(x)
	slowPrint() 
	my_next = raw_input(':')
	# clear the screen
	os.system('clear')
	
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
slowPrintMsgString("\n\nThanking you all for watching presentation Mark Harrington " + dt_string +"\n\n" )

time.sleep(10)

# clear the screen
os.system('clear')
	








