import sys,time,random, winsound

#important definitions ingame.
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
#StartMenu
from startmenu import *
#Intro
def intro():
    winsound.PlaySound(intromusic, winsound.SND_ASYNC)
    print_slow("This is the story of our past. Your past.\n")
    print_slow("In the beginning there was Light and Darkness.\n")
    print_slow("The light was followed by those that seeked to do good.\n")
    print_slow("But those that didn't fell into the darkness...\n")
    print_slow("Overtime the darkness grew stronger. Feeding on the weak.\n")
    print_slow("Once the darkness became powerful, it created a race of Dreg Lords.\n")
    print_slow("The Dreg Lord's created havok among those in the light.\n")
    print_slow("Overtime the Light started to dwindle to a flicker.\n")
    print_slow("But that flicker stayed bright, and manifested in someones heart.\n")
    time.sleep(1.5)
    print_slow("This is your heart.\n")
    time.sleep(1)
    print_slow("You are the one that will bring balance to the world.\n")
    time.sleep(2)
    print_slow("But it will not be easy.\n")
    time.sleep(3)
    print_slow("Make sure to never forget.\n")
    time.sleep(2)
    print_slow("You are the light.\n")
    time.sleep(5)
def battle(health_player,attack_player, inventory, weapon, lesserhealingpotion, healingpotion, greaterhealingpotion, lessermanapotion, manapotion, greatermanapotion ,magic_player,speed_player, health, attack, magic, name, speed, hits, criticalsaying, critical):
    x=0
    y=0
    if speed_player>=speed:
        player_turn=True
    else:
        player_turn=False
#Moster's Turn
    while True:
        x=0
        y=0
        time.sleep(0.5)
        if player_turn==False:
            for i in range(0,1):
                time.sleep(0.5)
                if name=="dragon" and health<=10:
                    critical=True
                if name=="dragon" and critical==True:
                    print(random.choice(criticalsaying))
                    time.sleep(1)
                    print("He looks kind of mad...")
                    time.sleep(2)
                    print(random.choice(hits))
                    time.sleep(0.3)
                    x=random.choice(attack)-10
                    health_player+=x
                    print("The " + name + " hit you with " + str(x) + " damage!")
                    player_turn=True
                    break
                if name=="troll" and health<=3:
                    critical=True
                if name=="troll" and critical==True:
                    print(random.choice(criticalsaying))
                    time.sleep(1)
                    print("He looks pretty mad...")
                    time.sleep(2)
                    print(random.choice(hits))
                    time.sleep(0.3)
                    x=random.choice(attack)-2
                    health_player+=x
                    print("The " + name + " hit you with " + str(x) + " damage!")
                    player_turn=True
                    break
            else:
                time.sleep(2)
                print(random.choice(hits))
                time.sleep(0.3)
                x=random.choice(attack)
                health_player+=x
                print("The " + name + " hit you with " + str(x) + " damage!")
                player_turn=True
#Player's Turn
        else:
            choice = None
            choice=input("What do you want to do? ")
            choice.lower()
            if choice=="attack":
                y=random.choice(attack_player)
                health+=y
                if y==0:
                    time.sleep(0.5)
                    print("You missed him!")
                    time.sleep(1)
                else:
                    time.sleep(0.5)
                    print("You hit the " + name + " with your " + weapon +" for " + str(y) + " damage!")
                    time.sleep(1)
                if health>=1:
                    print("Watch out he is going to attack!")
#potions inventory
            elif choice=="potion":
                if inventory>=1:
                    time.sleep(0.5)
                    print("which potion would you like to use?")
                    if lesserhealingpotion>=1:
                        print(lesserhealingpotionname)
                    if healingpotion>=1:
                        print(healingpotionname)
                    if greaterhealingpotion>=1:
                        print(greaterhealingpotionname)
                    if lessermanapotion>=1:
                        print(lessermanapotionname)
                    if manapotion>=1:
                        print(manapotionname)
                    if greatermanapotion>=1:
                        print(greatermanapotionname)
                    if distractionpotion>=1:
                        print(distractionpotionname)
                    print("8. Just kidding I don't want a potion.")
                    choice0=input("Type a number to choose: ")
                    if choice0=="1" and lesserhealingpotion>=1:
                        print("You use a Lesser Healing Potion.")
                        health_player+=3
                    elif choice0=="2" and healingpotion>=1:
                        print("You use a Healing Potion.")
                        health_player+=10
                    elif choice0=="3" and greaterhealingpotion>=1:
                        print("You use a Greater Healing Potion.")
                        health_player+=100
                    elif choice0=="4" and lessermanapotion>=1:
                        print("You use a Lesser Mana Potion.")
                        magic_player+=2
                    elif choice0=="5"and manapotion>=1:
                        print("You use a Mana Potion.")
                        magic_player+=5
                    elif choice0=="6"and greatermanapotion>=1:
                        print("You use a Greater Mana Potion.")
                        magic_player+=30
                    elif choice0=="7" and distractionpotion>=1:
                        print("You use a Distraction Potion and successfully get away.")
                        break
                    elif choice0=="1" and lesserhealingpotion<1:
                        print("You don't have Lesser Healing Potion!")
                        continue
                    elif choice0=="2" and healingpotion<1:
                        print("You don't have a Healing Potion!")
                        continue
                    elif choice0=="3" and greaterhealingpotion<1:
                        print("You don't have a Greater Heaing Potion!")
                        continue
                    elif choice0=="4" and lessermanapotion<1:
                        print("You don't have Lesser Mana Potion!")
                        continue
                    elif choice0=="5"and manapotion<1:
                        print("You don't have a Mana Potion!")
                        continue
                    elif choice0=="6" and greatermanapotion<1:
                        print("You don't have a Greater Mana Potion!")
                        continue
                    elif choice0=="7" and distractionpotion<1:
                        print("You don't have a distraction potion!")
                        continue
                    elif choice0=="8":
                        continue
                    else:
                        print("Please type a potion")
                        continue   
                else:
                    print("You don't have any potions!")
#magic
            elif choice=="magic":
                if magic_player>=1:
                    choice0=input("What spell would you like to cast? ")
                    if choice0=="scan":
                        if magic_player>=3:
                            print("You use your magic to scan the monster.")
                            time.sleep(0.3)
                            print("Poof")
                            time.sleep(0.5)
                            print("You think to yourself")
                            time.sleep(1)
                            print("The moster has " + str(health) + " life left.")
                            time.sleep(1)
                            print("He might do " + str(attack) + " damage in battle.")
                            time.sleep(1)
                            if magic>=1:
                                print("He has " + str(magic) + " left.")
                            else:
                                print("He does not have any magic left.")
                            magic_player-=3
                            time.sleep(0.5)
                            print("You used all that time to scan him! He is attacking!")
                            time.sleep(2)
                else:
                    print("You are out of magic!")
#choices
            elif choice=="health":
                print("Your health is: " + str(health_player))
                continue
            elif choice=="mana":
                print("You have " + str(magic_player) + "mana.")
                continue
            elif choice=="run":
                if speed_player>=speed:
                    print("You successfully ran away.")
                    break
                else:
                    print("You attempt running away but he is too fast and caught up, try using a distraction potion!")
            elif choice=="help":
                print("All you have to do is type a command. When entered you will do an action.")
                print("Your commands are:")
                print("'Attack'=Will attack enemy.")
                print("'Potion'=Will allow you to use potions in your inventory.")
                print("'Magic'=Will allow you to use magic.")
                print("'Health'=Will show current Health value.")
                print("'Mana'=Will show current Mana value.")
                print("'Run'=Will attempt to run away if your speed is faster than the enemy.")
                
                
            else:
                print("That is not a command!")
                continue
                
                
              
            player_turn=False
            
            
        if health_player<=0:
            print("You have died")
            break
        if health<=0:
            print("You defeated the " + name + "!")
            if name=="troll":
                stickloot=random.randint(0,25)
                if stickloot==16:
                    yorn=input("The troll dropped a stick! equiped?")
                    yorn.lower()
                    if yorn=="y" or yorno=="yes":
                        weapon="stick"
                    elif yorn=="n" or yorno=="no":
                        break
                    else:
                        print("Yes or No only please.")
                        continue
                swordloot=random.randint(0,100)
                if swordloot==76:
                    yorn=input("The troll dropped a sword! equiped?")
                    yorn.lower()
                    if yorn=="y" or yorno=="yes":
                        weapon="sword"
                        break
                    elif yorn=="n" or yorno=="no":
                        break
                    else:
                        print("Yes or No only please.")
                        continue
                swordloot=random.randint(0,10000000)
                
                
            break
        

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
lesserhealingpotion=3                         
healingpotion=0
greaterhealingpotion=0
lessermanapotion=3
manapotion=0
greatermanapotion=0
distractionpotion=1
inventory=lesserhealingpotion+healingpotion+greaterhealingpotion+lessermanapotion+manapotion+greatermanapotion+distractionpotion
scanmachine=False
#magic
scan=True
fireball=False
shield=False
avadacadavera=False

def dragon_encounter():
    name="dragon"
    magic=0
    health=30
    attack=[-3,-10,-10, -10, -10, -10, -10, -10, -10, -10, -10, -50]
    speed=20
    critical=False
    criticalsaying=['"ROOOOOOAAARRRR"', '"PREPARE TO DIE MORTAL"', '*Dragon prepares to bite hard*', '"YOU SHALL NOW FEEL TRUE PAIN"']
    print("You've stumbled across a dragon!")
    print("Health: " + str(health_player))
    battle(health_player, attack_player, inventory, weapon, lesserhealingpotion, healingpotion, greaterhealingpotion, lessermanapotion, manapotion, greatermanapotion, magic_player, speed_player, health, attack, magic, name, speed, hits, criticalsaying, critical)
def troll_encounter():
    name="troll"
    magic=2
    health=5
    attack=[-1, -2]
    speed=3
    critical=health-2
    criticalsaying=["STOP MON YOU HURTIN ME.", "WHY WON'T YOU JUST LET ME KILL YOU.", "RRRRRR"]
    print("You've stumbled across a troll!")
    print("Health: " + str(health_player))
    battle(health_player, attack_player, inventory, weapon, lesserhealingpotion, healingpotion, greaterhealingpotion, lessermanapotion, manapotion, greatermanapotion, magic_player, speed_player, health, attack, magic, name, speed, hits, criticalsaying, critical)

#music
gamestartmusic="C:/Users/caleb_000/Desktop/Game/Skyrim Theme 8-Bit.wav"
intromusic="C:/Users/caleb_000/Desktop/Game/8-Bit Mix- Music Box - Dark Cloud.wav"
normaldaymusic="C:/Users/caleb_000/Desktop/Game/Dark Cloud Main Theme 8 Bit Remix (1).wav"
beginningbattlemusic="C:/Users/caleb_000/Desktop/Game/Kingdom Hearts 2 -  The Encounter  8-bit.wav"
startmenu()
while True:

    time.sleep(2)
    print_slow("COCKADOODLEDOOOOOOOOOO\n")
    winsound.PlaySound(normaldaymusic, winsound.SND_ASYNC)
    time.sleep(3)
    print("*You slowly get out of bed, ready for today.*")
    time.sleep(3)
    print("*It is a beautiful day. A perfect day to go chop some wood for the cold nights.*")
    time.sleep(3)
    print("*You eat some eggs you found yesterday, then grab your axe and head outside to cut some wood.*")
    time.sleep(4)
    print("*As you walk through the forest you hear something out of the ordinary but can't tell what it is*")
    time.sleep(4)
    print("*You notice a nice big tree and prepare your axe.*")
    time.sleep(3)
    print("WACK")
    time.sleep(2)
    print("WACK")
    time.sleep(2)
    print("WACK")
    time.sleep(2)
    print("CRACKLE.... CRASH!")
    time.sleep(2)
    print("In 3 mighty blows you take down the tree.")
    time.sleep(2)
    print("You then hear something in the distance now. You pause to listen.")
    time.sleep(3)
    print("*It sounds like an old man, so you go to check out what is going on.*")
    time.sleep(3)
    winsound.PlaySound(beginningbattlemusic, winsound.SND_ASYNC)
    print_slow("Old Man: HEELLLLPPPP\n")
    time.sleep(1)
    print("*You sprint to where you hear the sound. You see an old man getting attacked by a troll*")
    time.sleep(1)
    print_slow("Old Man: Quick fight off this troll and I will reward you!\n")
    a=input("Will you help the old man?")
    a.lower()
    counter=0
    for i in range(0,3):
        if a=="yes" or a=="y":
            troll_encounter()
        elif counter==0:
            print_slow("Old Man: Please! It's going to kill me!\n")
            counter+=1
            continue
        elif counter==1:
            print_slow("Old Man: I'll give you 20 gold if you do!\n")
            counter+=1
            continue
        else:
            print("*You walk away from the old man. As you walk away you can hear the old man say something under his breath, but you can't make it out.*")
            time.sleep(2)
            print("*You then began to chop wood for the fire.*")
            time.sleep(2)
            print("*You swing back and then.*")
            print("POOF")
            print("*The Tree comes to life and grabs you.*")
            print_slow("Old Man: You have made a bad choice by not helping me... Now you will die.")
            break
            break
        
    troll_encounter()
    print_slow("Hello there young traveler. What is your name? ")
    name_player=input("")
    print_slow("Well it's nice to meet you, " + name_player)


    troll_encounter()




