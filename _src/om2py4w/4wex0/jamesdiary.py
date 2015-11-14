# -*- coding: utf-8 -*-

import sys
import time
import os

if not os.path.exists('diary.txt'):
    target= open('diary.txt', 'a')
    target.close()


def writediary(data):
    target = open("diary.txt", 'a+')
    print "what do u want to say TODAY?"

    print "I'm going to write these to the file diary.txt."

    target.write(data+"  ")
    target.write(time.strftime("%Y/%m/%d%H:%M:%S"))
    target.write("\n")


def readdiary():
    target = open("diary.txt")
    return target.read()


def main():
    line2=""
    line1=""

    target = open("diary.txt", 'a+')	

    writediary()

    print "here is what you have written"
    readdiary()

    while True:
        line2 = raw_input("do u want to continue?if you want to continue print Y, want to quit print N ")
        if line2=="Y":
    	    writediary()
    	    print "here is what you have written"
    	    readdiary()

        elif line2=="N":
    	    target.close()
    	    break
    	


    print "And finally, we close it."
    #target.close()


if __name__ == '__main__':
    main()

