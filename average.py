print("Enter your name")
name= (input())
print("Enter your marks")
print("English?")
a=int(input())
print("kiswa?")
b=int(input())
print("math?")
c=int(input())
print("bio?")
d=int(input())
print("chem?")
e=int(input())
sum=a+b+c+c+d+e
print(name)
print("Total",sum)
avg=sum/5
print("AVERAGE", sum/5)

if avg >=70 and avg<=100:
	print("Your Grade is A")
elif avg >=60 and avg<69:
	print("Your Grade is B")
elif avg >=50 and avg<59:
	print("Your Grade is C")
elif avg >=40 and avg<49: 
	print("Your Grade is D")
elif avg >=30 and avg<39:
	print("Your Grade is E,FAIL")
