# -*- coding: utf-8 -*-

import sys
import time

line2=""
line1=""

target = open("diary.txt", 'a+')

def writedairy():
	target = open("diary.txt", 'a+')
	print "what do u want to say TODAY?"
	line1 = raw_input("line 1: ")

	print "I'm going to write these to the file diary.txt."

	target.write(line1+"  ")
	target.write(time.strftime("%Y/%m/%d%H:%M:%S"))
	target.write("\n")
	
	#print "here is what you have written"
	#target = open("diary.txt", 'a+')
	#print target.read()

#def askforcontinue():
	#print "do u want to continue?if you want to continue print Y, want to quit print N"
	#line2 = raw_input("Y/N ")

writedairy()
#askforcontinue()
print "here is what you have written"
target = open("diary.txt")
print target.read()

while True:
	line2 = raw_input("do u want to continue?if you want to continue print Y, want to quit print N ")
	if line2=="Y":
		writedairy()
		print "here is what you have written"
		target = open("diary.txt")
		print target.read()
	elif line2=="N":
		target.close()
		break
		print "And finally, we close it."


print "And finally, we close it."
#target.close()
