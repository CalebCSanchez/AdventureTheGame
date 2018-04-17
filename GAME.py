from startmenu import *
from intro import *
from tutorial_encounter import *
from BasicImports import *







#STARTING GAME STATS
#sayings
hits=["WACK", "SCRATCH", "POW", "WAM", "BANG"]
dragoncritical=['"ROOOOOOAAARRRR"', '"PREPARE TO DIE MORTAL"', '*Dragon prepares to bite hard*', '"YOU SHALL NOW FEEL TRUE PAIN"']
dragondeath="Ouchy."
#potions
lesserhealingpotionname="1) Lesser Healing Potion"
healingpotionname="2) Healing Potion"
greaterhealingpotionname="3) Greater Healing Potion"
lessermanapotionname="4) Lesser Mana Potion"
manapotionname="5) Mana Potion"
manahealingpotionname="6) Greater Mana Potion"
distractionpotionname="7) Distraction Potion"
#Player
health_player=100
attack_player=0
magic_player=10
speed_player=10
#weapons
weapon="axe"
if weapon=="fists":
    attack_player=[-1,-1,-1,-2]
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









#THE GAME

def GAME():
    while True:
        intro()
        print_slow("COCKADOODLEDOOOOOOOOOO\n")
        PlaySound(normaldaymusic, SND_ASYNC)
        sleep(3)
        print("*You slowly get out of bed, ready for today.*")
        sleep(3)
        print("*It is a beautiful day. A perfect day to go chop some wood for the cold nights.*")
        sleep(3)
        print("*You eat some eggs you found yesterday, then grab your axe and head outside to cut some wood.*")
        sleep(4)
        print("*As you walk through the forest you hear something out of the ordinary but can't tell what it is*")
        sleep(4)
        print("*You notice a nice big tree and prepare your axe.*")
        sleep(3)
        print("WACK")
        sleep(2)
        print("WACK")
        sleep(2)
        print("WACK")
        sleep(2)
        print("CRACKLE.... CRASH!")
        sleep(2)
        print("*In 3 mighty blows you take down the tree.*")
        sleep(2)
        print("*You then hear something in the distance now. You pause to listen.*")
        sleep(3)
        PlaySound(beginningbattlemusic, SND_ASYNC | SND_LOOP)
        print_slow("Old Man: HEELLLLPPPP\n")
        sleep(1)
        print("*You sprint to where you hear the sound. You see an old man getting attacked by a bat*")
        sleep(3)
        print_slow("Old Man: Quick fight off this bat and I will reward you!\n")
        counter=0
        while True:
            print("Will you help athe old man?")
            a=input("1.Yes 2.No\n")
            a.lower()
            if a=="1":
                tutorial_encounter(health_player, weapon, attack_player, healingpotion, healingpotionname, hits, inventory)
                break
            elif counter==0:
                print_slow("Old Man: Please! It's going to kill me!\n")
                counter+=1
                continue
            elif counter==1:
                print_slow("Old Man: I'll give you 20 gold if you just say yes!!\n")
                counter+=1
                continue
            else:
                print("*You walk away from the old man. As you walk away you can hear the old man say something under his breath, but you can't make it out.*")
                sleep(4)
                PlaySound(normaldaymusic, SND_ASYNC)
                print("*You then began to chop wood for the fire.*")
                sleep(3)
                print("*You swing back and then.*")
                sleep(2)
                PlaySound(wizardmusic, SND_ASYNC)
                print("POOF")
                sleep(2)
                print("*The Tree comes to life and grabs you.*")
                sleep(2)
                print("*As you struggle to escape you hear a whisper in your ear.*")
                sleep(3)
                print_slow("Old Man: You have made a bad choice by not helping me... Now you will die.\n")
                PlaySound(None, SND_ASYNC)
                print("YOU HAVE DIED.")
                continue1=input("Continue?\n")
                continue1.lower()
                if continue1=="yes" or continue1=="y":
                    break
                    break
                sleep(10)
                exit()
        endgame()
