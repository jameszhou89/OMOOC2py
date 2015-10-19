# -*- coding: utf-8 -*-
total=0
numbers=[]
while(True):
    number= raw_input("what is the number in you mind now?:")
    if number == "0": break
    number=int(number)
    numbers.append(number)
    print numbers  
for i in numbers:
	total=total+i
print total
