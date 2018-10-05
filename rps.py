import random
a={1:'r',2:'p',3:'s'}
c=a[random.randint(1,3)]
p=input("enter 'r' or 'p' or 's'")

if(c==a):
		print("tie")
	
elif(c=='r'and a=='s') or(c=='p'and a=='r') or(c=='s'and a=='p'):
	print("computer win")
else:
	print("you won")