a=['1','2','3','4','5','6','7','8','9']
def print_Board():
    print(a[0],'|',a[1],'|',a[2])
    print("........")
    print(a[3],'|',a[4],'|',a[5])
    print("........")
    print(a[6],'|',a[7],'|',a[8])
PlayerOneTurn = True
while True:
        print_Board()
        p=input("choose an available place")
        if(p in a):
            if(a[int(p)-1]=='x' or a[int(p)-1]=='o'):
                print("place taken, choose another place")
                continue
            else:
                    if PlayerOneTurn:
                            print("player 1>>")
                            a[int(p)-1]= 'x'
                            PlayerOneTurn = not PlayerOneTurn
                    else:
                            print("player 2 >>")
                            a[int(p)-1]= 'o'
                            PlayerOneTurn = not PlayerOneTurn
                    for i in (0,3,6):
                            if(a[i]==a[i+1] and a[i]==a[i+2]):
                                    print("Game over")
                                    exit()
                    for i in range (3):
                            if(a[i]==a[i+3] and a[i]==a[i+6]):
                                    print("Game over")
                                    exit()
                    if(a[0]==a[4] and a[0]==a[8]):
                                    print("game over")   
                                    exit()
                    if(a[2]==a[4] and a[2]==a[6]):
                                    print("game over")
                                    exit()
        else:
                 print("you have entered an invalied position")
                 continue
               cl308@soetcse:~/pramodh$ python3 ttt.py
1 | 2 | 3
........
4 | 5 | 6
........
7 | 8 | 9
choose an available place1
player 1>>
Traceback (most recent call last):
  File "ttt.py", line 20, in <module>
    playerOneTurn= notlpayerOneTurn
NameError: name 'notlpayerOneTurn' is not defined
cl308@soetcse:~/pramodh$ python3 ttt.py
1 | 2 | 3
........
4 | 5 | 6
........
7 | 8 | 9
choose an available placehj
you have entered an invalied position
1 | 2 | 3
........
4 | 5 | 6
........
7 | 8 | 9
choose an available place3
player 1>>
Traceback (most recent call last):
  File "ttt.py", line 20, in <module>
    PlayerOneTurn = not PlayerOneTurn
NameError: name 'notlpayerOneTurn' is not defined
cl308@soetcse:~/pramodh$ python3 ttt.py
1 | 2 | 3
........
4 | 5 | 6
........
7 | 8 | 9
choose an available place9
player 1>>
1 | 2 | 3
........
4 | 5 | 6
........
7 | 8 | x
choose an available place4
player 2 >>
1 | 2 | 3
........
o | 5 | 6
........
7 | 8 | x
choose an available place4
you have entered an invalied position
1 | 2 | 3
........
o | 5 | 6
........
7 | 8 | x
choose an available place5
player 1>>
1 | 2 | 3
........
o | x | 6
........
7 | 8 | x
choose an available place6
player 2 >>
1 | 2 | 3
........
o | x | o
........
7 | 8 | x
choose an available place7
player 1>>
1 | 2 | 3
........
o | x | o
........
x | 8 | x
choose an available place7
you have entered an invalied position
1 | 2 | 3
........
o | x | o
........
x | 8 | x
choose an available place8
player 2 >>
1 | 2 | 3
........
o | x | o
........
x | o | x
choose an available place9
you have entered an invalied position
1 | 2 | 3
........
o | x | o
........
x | o | x
choose an available place1
player 1>>
game over
cl308@soetcse:~/pramodh$   
        
