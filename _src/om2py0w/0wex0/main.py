total=0
numbers=[]
number= raw_input("what is the number in you mind now?")
if number=="done" ： break
numbers.append(number)
for i in numbers:
	total=total+i
print total