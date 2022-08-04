import random

def Winner(Computer, Player):
    if Computer == Player:
        return None
    elif Computer == 'S':
        if Player == 'W':
            return False
        elif Player == 'G':
            return True
    elif Computer == 'W':
        if Player == 'G':
            return False
        elif Player == 'S':
            return True
    elif Computer == 'G':
        if Player == 'S':
            return False
        elif Player == 'W':
            return True

print("Computer Turn! Snake(S) Water(W) and Gun(g)")
randNo = random.randint(1, 3)
print(randNo)
if randNo == 1:
    Computer = 'S'
elif randNo == 2:
    Computer = 'W'
elif randNo == 3:
    Computer = 'G'

Player = input("Your Turn: Snake(S) Water(W) and Gun(G)")
Result = Winner(Computer, Player)

print(f"Computer Choise {Computer} ")
print(f"Your Choise {Player}")
if Result == None:
    print("The Game is Tie! Thanks You")
elif Result:
    print("You Win.. Good Play!")
else:
    print("You Lose... Play again!")         