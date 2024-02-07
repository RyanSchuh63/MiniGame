import random

#Player Stats
p1hp = 20
p1atk = 0
p1def = 5
p2hp = 20
p2atk = 0
p2def = 5

#Class Stats & List
katk = 0
kdef = 10
ratk = 5
rdef = 5
classlist = "Knight & Rogue"
print(classlist)

#Input for players to choose class and assign their stats
p1class = input("Player 1 choose your class: ")
p2class = input("Player 2 choose your class: ")

if p1class == "Knight":
    p1atk = p1atk + katk
    p1def = p1def + kdef
elif p1class == "Rogue":
    p1atk = p1atk + ratk
    p1def = p1def + rdef
    
if p2class == "Knight":
    p2atk = p2atk + katk
    p2def = p2def + kdef
elif p2class == "Rogue":
    p2atk = p2atk + ratk
    p2def = p2def + rdef
print("P1 Stats:", "ATK", p1atk, "DEF", str(p1def) + ".", "P2 Stats:", "ATK", p2atk, "DEF", str(p2def) + ".")

#Sets up Initiative which determines who goes first
p1init = 0
p2init = 0
while p1init == p2init:
    roll = random.randint(1,20)
    p1init = roll
    currentplayer = 2
    roll2 = random.randint(1,20)
    p2init = roll2
    currentplayer = 1
    print("P1 Initiative:", str(p1init) + ".", "P2 Initiative:", str(p2init) + ".")

if p1init > p2init:
    print("Player 1 Starts")
    currentplayer = 1
elif p2init > p1init:
    print("Player 2 Starts")
    currentplayer = 2


#Loop for combat
while p1hp > 0 and p2hp > 0:
    def player_atk():
        return random.randint(1, 20)

    def player_dmg():
        return random.randint(1,10)
    
    def Hit():
        if currentplayer == 1:
            return player_atk() + p1atk
        elif currentplayer == 2:
            return player_atk() + p2atk
    
    if currentplayer == 1:
        print("Player 1 rolled a", Hit(), "to attack and", player_dmg(), "for damage.")
    elif currentplayer == 2:
        print("Player 2 rolled a", Hit(), "to attack and", player_dmg(), "for damage.")
    
    if currentplayer == 1:
        if Hit() > p2def:
             p2hp -= (player_dmg() + p1atk)  
             print("Thats a Hit Player 2 now has", p2hp, "HP left!")
             currentplayer = 2
        else:
            print("Player 1 Missed")
            currentplayer = 2
    elif currentplayer == 2:
        if Hit() > p1def:
            p1hp -= (player_dmg() + p2atk)
            print("Thats a Hit Player 1 now has", p1hp, "HP left!")
            currentplayer = 1
        else:
            print("Player 2 Missed")
            currentplayer = 1

#Decides winner            
if p1hp <= 0:
    print("Player 2 Wins!!!")
elif p2hp <= 0:
    print("Player 1 wins")
    