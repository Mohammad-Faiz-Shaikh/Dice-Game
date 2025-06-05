from random import randint
# rules
print(''' GAME RULES 
1. Choose a target score.
2. Each player rolls the dice in order.
3. Rolling a 6 gives an extra turn (up to 2 times).
4. Rolls that exceed the target are discarded.
5. First player to exactly reach the target wins!''')
player=int(input("Enter the number of players : "))
lst = []
# storing the name of the players
for i in range(1,player+1):
    value=input(f"enter player {i} name : ")
    lst.append(value)
    print(lst)
#choosing target
target=int(input("Enter a Number as the Target: "))
# sum variables    

a="y"
while(a.lower()=="y"):
    total=0
    winner=""
    while(total!= target):
        for i in lst:
            extra=0
            while True:
                print(f"\n Player {i} ,press enter to roll the dice")
                input()
                n=randint(1,6)
                print(f"The dice gave: {n}")
                if(total+n>target):
                    print("The Total Exceeds the Target")
                    print(f"Sum Became: {total}")
                    break
                else:
                    total=total+n
                    print(f"Sum Became: {total}")
                if total == target:
                    winner = i
                    break
                if n==6:
                    extra+=1
                    if (extra<3):
                        print(f"{i} Whooo You Got an Extra Turn")
                        print(f"Sum Became: {total}")
                        continue
                    else:
                        print("No More 6")
                break
            if winner:
                break 
        if winner:
            break 
    print(f"Congratulations! The Winner is {winner}")
    a=input("Press Y and enter to play again: ")    