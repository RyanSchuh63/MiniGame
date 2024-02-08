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
classlist = "Knight or Rogue"
print("Choose a class", classlist)

#Input for players to choose a class
p1class = input("Player 1 choose your class: ")
p2class = input("Player 2 choose your class: ")

#Assigns stats based on class picked
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

#Displays both player's stats
print("P1 Stats:", "ATK", p1atk, "DEF", str(p1def) + ".", "P2 Stats:", "ATK", p2atk, "DEF", str(p2def) + ".")

#Determines the order of combat
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

#Displays who is going first
if p1init > p2init:
    print("Player 1 Starts")
    currentplayer = 1
elif p2init > p1init:
    print("Player 2 Starts")
    currentplayer = 2

#Functions That calculates attack accuracy
def player_atk(currentplayer, p1atk, p2atk):
    if currentplayer == 1:
        return random.randint(1, 20) + p1atk
    elif currentplayer == 2:
        return random.randint(1, 20) + p2atk

#Function calculates attack damage
def player_dmg(currentplayer, atk_value, p1def, p2def):
    if currentplayer == 1:
        return random.randint(1,10) + p1atk
    elif currentplayer == 2:
        return random.randint(1,10) + p2atk

#Loop for combat
while p1hp > 0 and p2hp > 0:
    #Variables that call accuracy & damage functions at the start of every turn
    atk_value = player_atk(currentplayer, p1atk, p2atk)

    dmg_value = player_dmg(currentplayer, atk_value, p1def, p2def)

    #Displays current player's attack accuracy
    print("Player", currentplayer, "rolled a", atk_value, "to attack")

    #Determines if attack is successful, calculates remaining health, & updates who the current player is
    if currentplayer == 1:
        if atk_value > p2def:
            p2hp -= dmg_value 
            print("Thats a Hit for", dmg_value, "damage Player 2 now has", p2hp, "HP left!")
            currentplayer = 2
        elif atk_value < p2def:
            print("Player 1 Missed")
            currentplayer = 2
    elif currentplayer == 2:
        if atk_value > p1def:
            p1hp -= dmg_value 
            print("Thats a Hit for", dmg_value, "damage Player 1 now has", p1hp, "HP left!")
            currentplayer = 1
        elif atk_value < p1def:
            print("Player 2 Missed")
            currentplayer = 1

#Displays winner            
if p1hp <= 0:
    print("Player 2 Wins!!!")
elif p2hp <= 0:
    print("Player 1 Wins!!!")
    
