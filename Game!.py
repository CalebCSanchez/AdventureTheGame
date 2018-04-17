from GAME import *
#Intro
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

#Test Area




#GAME
counter=0
os.chdir("./Music/")
startmenu()
while True:
    print("1.NEW GAME | 2.LOAD GAME | 3.CREDITS | 4.HOW TO PLAY | 5.EXIT")
    startmenuoption=input("")
    startmenuoption.lower()
    if startmenuoption=="1":
        GAME()
    elif startmenuoption=="2":
        print_medium("COMING SOON :)\n")
        sleep(2)
    elif startmenuoption=="3":
        while True:
            for i in range(0,50):
                sleep(0.01)
                print("")
            print_slow("Created by Caleb Sanchez.\n")
            sleep(2)
            print_slow("Yeah... that's about it...\n")
            print_slow("Oh yeah, and we don't own the rights to the music. All songs and sound effects have been taken from youtube sources. Please don't sue me.\n")
            break
    elif startmenuoption=="4" or startmenuoption=="howtoplay" or startmenuoption=="howto play" or startmenuoption=="how toplay" or startmenuoption=="how to play":
        print_medium("Please do not type anything unless given the option too.\n")
        print_medium("You can mess up the game by typing too early.\n")
        print_medium("And since there is no save you probably don't want to do that...\n")
        print_medium("When given the option too, just type the number infront of the option.\n")
        print_medium("Unless you know what you're doing, I would accept someones help when offered ;)\n")
        print_medium("Also the mouse is not needed so please don't click anything.\n")
        print_medium("Alright, get out there kid.\n")
        sleep(5)
        
    elif startmenuoption=="exit" or startmenuoption=="5":
        PlaySound(None, SND_ASYNC)
        exit()
    else:
        if counter>=0 and counter<=3:
            print("Please type the number '4'")
            counter+=1
        else:
            print_slow("Alright thanks for playing :^)       ")
            PlaySound(None, SND_ASYNC)
            exit()
            
            
            
            







