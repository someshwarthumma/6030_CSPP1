nivas = open("out.txt","r")
some = open("sout.txt","r")

for line in nivas:
	if line not in some:
		print(line)