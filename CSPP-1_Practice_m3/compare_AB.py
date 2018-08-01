varA=input("enter the value of VarA")
varB=input("enter the value of VarB")
type_of_A=type(varA)
type_of_B=type(varB)
if type_of_A==str or type_of_B==str:
	print("string involved")
elif varA>varB :
	print("bigger")
elif varA==varB:
	print("Equal")
elif varA<varB:
	print("smaller")