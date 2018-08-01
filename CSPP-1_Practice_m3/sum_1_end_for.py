end=int(input('enter value of end: '))
var=0
total=0
for var in range(1,end+1):
	total=total+var
	var=var+1
print(total)