#Player
health_player=100
maxhealth_player=100
attack_player=0
magic_player=10
speed_player=10
#weapons
weapon="axe"
if weapon=="fists":
    attack_player=[-1,-1,-1,-2]
    l
if weapon=="stick":
    attack_player=[0,-1,-1,-1,-2]
if weapon=="axe":
    attack_player=[0,-5,-5,-5,-5,-10]
if weapon=="sword":
    attack_player=[0,-3,-3,-3,-3,-3,-5,-5,-5,-10]
if weapon=="The Ultimate Weapon":
    attack_player=-100
#inventory
lesserhealingpotion=0                        
healingpotion=0
greaterhealingpotion=0
lessermanapotion=0
manapotion=0
greatermanapotion=0
distractionpotion=0
inventory=lesserhealingpotion+healingpotion+greaterhealingpotion+lessermanapotion+manapotion+greatermanapotion+distractionpotion
scanmachine=False
#magic
scan=False
fireball=False
shield=False
avadacadavera=False
#Enchants

def savecodefuction():
    
    print("Your savecode is: ")                                                      ")
def loadfunction():
    load=input("Please type your savecode you were given: ")
    player_health=load[0:9]
    maxhealth_player=load[0:9]
