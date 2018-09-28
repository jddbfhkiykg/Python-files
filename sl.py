import random 
count=0
while (count<=100):
	n=input("enter r to roll a dice")
	if(n=='r'):
		a=random.randint(1,6)
		count=count+a
		print("my position"),count
		print("your random value",a)


	if (count==11):
		count=2
		print("snake bitten")

	elif(count==8):
		count=37
		print("climb the ladder")


	elif(count==13):
		count=34
		print("climb the ladder")

	elif(count==25):
		count=4
		print("snake bitten")

	elif(count==38):
		count=9
		print("snake bitten")

	elif(count==40):
		count=68
		print("climb the ladder")

	elif(count==52):
		count=81
		print("climb the ladder")

	elif(count==65):
		count=46
		print("snake bitten")

	elif(count==76):
		count=97
		print("climb the ladder")

	elif(count==89):
		count=70
		print("snake bitten")

	elif(count==93):
		count=64
		print("snake bitten")

	else:
		count=100
		print("i won the game")