import sys 
import time


target = open("diary.txt", 'a+')

print "Now I'm going to ask you for 1 lines."

line1 = raw_input("line 1: ")

print "I'm going to write these to the file."

target.write(line1+"  ")
target.write(time.strftime("%Y/%m/%d%H:%M:%S"))
target.write("\n")
