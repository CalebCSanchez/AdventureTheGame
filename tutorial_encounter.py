from BasicImports import *
def tutorial_encounter(health_player, weapon,attack_player, healingpotion, healingpotionname, hits, inventory):
    sleep(1)
    print("You have ecountered a large bat!")
    name="bat"
    health=35
    attack=[-3,-5,-5,-5,-3,0,-3,-3,-3,-3,-10]
    speed=0
    attacksounds=["Screech!", "*flaps wings*", ""]
    print_medium("Old Man: Would you like some help fighting? \n")
    counter=0
    x=0
    y=0
    while True:
        help1=input("1.Yes  2.No \n")
        help1.lower()
        if help1=="1":
            print_slow("Old Man: You enter battle by stumbling across an enemy.\n")
            print_slow("Old Man: All you have to do is hit your enemy until it dies.\n")
            print_slow("Old Man: But watch out, they are trying to do the same thing to you.\n")
            print_slow("Old Man: Here let me cast a spell on you.\n")
            sleep(1)
            print("Poof")
            sleep(0.7)
            print("Health: " + str(health_player))
            sleep(0.7)
            print("*did he just cast a spell?*")
            sleep(0.7)
            print_slow("Old Man: That shows how much you have left in you until you die. It should show up now before every battle \n")
            print_slow("Old Man: Watch out!\n")
            sleep(1)
            print(choice(attacksounds))
            sleep(2)
            print("SCRATCH")
            x=-5
            health_player+=x
            print("The " + name + " hit you with " + str(x) + " damage!")
            sleep(2)
            print_slow("Old Man: That looks like it hurt. Let's check how much health you have. Choose the 'health' option.\n")
            counter1=0
            while True:
                choice=input("You: ")
                choice.lower()
                if choice=="health":
                    print("Health: " + str(health_player))
                    break
                else:
                    if counter1==0:
                        print_medium("Just type the word 'health'\n")
                        counter1+=1
                    elif counter1==1:
                        print_medium("It's not that hard kid... just say 'health'\n")
                        counter1+=1
                    elif counter1==2:
                        print_medium("Old Man: Look just pray to your god and tell them to type 'health' without the quotes!\n")
                        counter1+=1
                    else:
                        print_medium("Old Man: You are useless...\n")
                        counter1-=3
            print_slow("Old Man: Now you know how to check your health during battle.\n")
            print_slow("Why don't you attempt attacking it? Think you could figure out how to do that?\n")
            while True:
                choice=input("You: ")
                choice.lower()
                if choice=="attack":
                    sleep(1)
                    print("You get ready to swing.")
                    sleep(2)
                    print("WACK")
                    y=-5
                    health+=y
                    sleep(0.7)
                    print("You hit the " + name + " with your " + weapon +" for " + str(y) + " damage!")
                    break
                else:
                    print_medium("Old Man: Just say 'attack'\n")
            print_slow("Old Man: Nice hit! But you can do better...\n")
            sleep(2)
            print("CHOMP")
            print("*CRITICAL*")
            x=-35
            health_player+=x
            print("The " + name + " hit you with " + str(x) + " damage!")
            sleep(1)
            print_slow("Old Man: Look's like you took some damage there, here take one of these.\n")
            healingpotion+=1
            print("*Equiped " + healingpotionname+"*")
            print_slow("Old Man: All you have to do is say 'potion' to open your potion inventory.\n")
            while True:
                choice=input("You: ")
                choice.lower()
                if choice=="potion":
                    if inventory>=1:
                        sleep(0.5)
                        print("which potion would you like to use?")
                        if healingpotion>=1:
                            print(healingpotionname)
                        choice0=input("Type a number to choose: ")
                        if choice0=="2" and healingpotion>=1:
                            print("You use a Healing Potion.")
                            health_player+=10
                            break
                        else:
                            print("Please put a number.")
                            continue   
                    else:
                        print("You don't have any potions!")
                else:
                    print_slow("Old Man: Just say 'potion'\n")
            print_slow("Old Man: Nice. Now check your health again.\n")
            while True:
                choice=input("You: ")
                choice.lower()
                if choice=="health":
                    print("Health: " + str(health_player))
                    break
                else:
                    print("Type 'health'")
            print_slow("Your health is still a little low. Here let me heal you a bit.\n")
            sleep(1)
            print("POOF")
            sleep(1)
            health_player=100
            print_slow("Alright that's all you need to know for now. Now finish him off!\n")
            break
        elif help1=="no" or help1=="nope" or help1=="n" or help1=="nah":
            print_medium("Old Man: Okay if you say so... Good Luck.\n")
            sleep(1)
            break
        else:
            print_slow("Old Man: Just say 'yes' or 'no'.\n")
#Battle
    player_turn=True
    counter1=0
    while True:
        x=0
        y=0
        if player_turn==False:
            if health<=0:
                print("You killed it!")
                break
            if health<=10:
                sleep(2)
                print("*flaps wings intensely*")
                x=random.choice(attack)+15
            else:
                sleep(2)
                print(random.choice(attacksounds))
                x=random.choice(attack)
            sleep(2)
            sleep(0.3)
            health_player+=x
            if x<0:
                print(random.choice(hits))
            print("The " + name + " hit you with " + str(x) + " damage!")
            counter1+=1
            player_turn=True
        else:
            counther=0
            for i in range(0,4):
                if health_player<=40:
                    print_slow("Old Man: You're health is low! Let me heal you.\n")
                    slow(1)
                    player_health=100
                    slow(1)
                choice=input("What do you want to do?\n ")
                choice.lower()
                if choice=="attack":
                    y=random.choice(attack_player)
                    health+=y
                    if y==0:
                        sleep(0.5)
                        print("You missed him!")
                        sleep(1)
                        if counter1==4:
                            print_slow("Old Man: It sure does have a lot of health. Let me scan him real quick.\n")
                            sleep(1)
                            print("Poof")
                            sleep(1)
                            print("Old Man: The moster has " + str(health) + " life left.\n")
                            sleep(1)
                            print_slow("Old Man: He might do " + str(attack) + " damage in battle.\n")
                            sleep(1)
                            print_slow("Old Man: Gosh that took a lot out of me... Don't except me to scan often.\n")
                        print("Watch out he is going to attack!")
                        break
                    else:
                        sleep(0.5)
                        sleep(2)
                        print(random.choice(hits))
                        sleep(0.3)
                        print("You hit the " + name + " with your " + weapon +" for " + str(y) + " damage!")
                        sleep(1)
                        if counter1==4:
                            print_slow("Old Man: It sure does have a lot of health. Let me scan him real quick.\n")
                            sleep(1)
                            print("Poof")
                            sleep(1)
                            print("Old Man: The moster has " + str(health) + " life left.\n")
                            sleep(1)
                            print_slow("Old Man: He might do " + str(attack) + " damage in battle.\n")
                            sleep(1)
                            print_slow("Old Man: Gosh that took a lot out of me... Don't except me to scan often.\n")
                        print("Watch out he is going to attack!")
                        break
                elif choice=="potion":
                    if inventory>=1:
                        while True:
                            sleep(0.5)
                            print("which potion would you like to use?")
                            if healingpotion>=1:
                                print(healingpotionname)
                            print("8. Just kidding I don't want a potion.")
                            choice0=input("Type a number to choose: ")
                            if choice0=="2" and healingpotion>=1:
                                print("You use a Healing Potion.")
                                health_player+=10
                                break
                            elif choice0=="8":
                                break
                            else:
                                print("Please put a number.")  
                    else:
                        print("You don't have any potions!")
                elif choice=="magic":
                    print("You don't know any magic!")
                elif choice=="health":
                    print("Your health is: " + str(health_player))
                elif choice=="mana":
                    print("You don't have any mana!")
                elif choice=="run":
                    print_slow("Old Man: You tryna run kid?\n")
                elif choice=="help":
                    print("All you have to do is type a command. When entered you will do an action.")
                    print("Your commands are:")
                    print("'Attack'=Will attack enemy.")
                    print("'Potion'=Will allow you to use potions in your inventory.")
                    print("'Health'=Will show current Health value.")
                elif counther<3:
                    print("Please type a command")
                else:
                    print("You took too long!")
                    
                counther+=1
            player_turn=False
        

                        
 
                        
            
                        
                        
                        

                    
                        
            
