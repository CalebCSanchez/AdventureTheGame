from BasicImports import *
from GAME import *
from AllMonsters import *
def battle(monster, health_player,attack_player, inventory, weapon, lesserhealingpotion, healingpotion, greaterhealingpotion, lessermanapotion, manapotion, greatermanapotion ,magic_player,speed_player): 
    monster()
    if speed_player>=speed:
        player_turn=True
    else:
        player_turn=False
    while True:
        x=0
        y=0
        sleep(0.5)
        #Monster's Turn
        if player_turn==False:
            sleep(0.5)
            if  critical==True:
                x=criticalattack
                print(choice(criticalsaying))
                sleep(2)
                print(choice(hits))
                health_player+=x
                print("The " + name + " hit you with " + str(x) + " damage!")
                player_turn=True
            else:
                sleep(2)
                print(choice(hits))
                sleep(0.3)
                x=choice(attack)
                health_player+=x
                print("The " + name + " hit you with " + str(x) + " damage!")
                player_turn=True
#Player's Turn
        else:
            for i in range(0,4):
                print("What do you want to do? ")
                choice=input("1)ATTACK | 2)POTION | 3)MAGIC | 4)HEALTH | 5)MANA | 6)RUN | 7)HELP")
                choice.lower()
                if choice=="1":
                    y=choice(attack_player)
                    health+=y
                    if y==0:
                        sleep(0.5)
                        print("You missed him!")
                        sleep(1)
                    else:
                        print(choice(hits))
                        sleep(0.5)
                        print("You hit the " + name + " with your " + weapon +" for " + str(y) + " damage!")
                        sleep(1)
                    if health>=1:
                        print("Watch out he is going to attack!")
    #potions inventory
                elif choice=="2":
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
                elif choice=="3":
                    if magic_player>=1:
                        if scan==True:
                            print("1)SCAN")
                        else:
                            print("You don't know any spells!")
                            break
                        choice0=input("What spell would you like to cast? ")
                        if choice0=="1":
                            if magic_player>=3:
                                print("You use your magic to scan the monster.")
                                sleep(0.3)
                                print("Poof")
                                sleep(0.5)
                                print("You think to yourself")
                                sleep(1)
                                print("The moster has " + str(health) + " life left.")
                                sleep(1)
                                print("He might do " + str(attack) + " damage in battle.")
                                sleep(1)
                                if magic>=1:
                                    print("He has " + str(magic) + " left.")
                                else:
                                    print("He does not have any magic left.")
                                magic_player-=3
                                sleep(0.5)
                                print("You used all that time to scan him! He is attacking!")
                                sleep(2)
                            else:
                                print("Not enough mana.")
                    else:
                        print("You are out of magic!")
    #choices
                elif choice=="4":
                    print("Your health is: " + str(health_player))
                    continue
                elif choice=="5":
                    print("You have " + str(magic_player) + "mana.")
                    continue
                elif choice=="6":
                    if speed_player>=speed:
                        print("You successfully ran away.")
                        break
                    else:
                        print("You attempt running away but he is too fast and caught up, try using a distraction potion!")
                elif choice=="7":
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
            break
        
battle(troll_encounter, health_player,attack_player, inventory, weapon, lesserhealingpotion, healingpotion, greaterhealingpotion, lessermanapotion, manapotion, greatermanapotion ,magic_player,speed_player)


