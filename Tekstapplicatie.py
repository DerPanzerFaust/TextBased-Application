def option_story_5():
    print("You decided to wait. That evening another bombing of the area was planned. No one survived the second waves of bombs.")
    print("GAME OVER")

def main_story_4():
    print("After a while of waiting you hear talking noices in the distance. You decide to check it out. When you arrive you see people in distress. You know to get out of the town as fast as possible, but you know the risk.\nThere's a boat leaving the country in 5 minutes. What do you do? Take the BOAT or STAY and wait what will happen next?")
    choice = input("BOAT or WAIT")
    print("Choose BOAT or WAIT")

    if choice == "BOAT":
        main_story_5
    elif choice == "WAIT":
        option_story_5

def main_story_3():
    main_story_4()

def option_story_4():
    print("You decided to run to an open field were you're hoping to be safe from the bombs. Bad luck! You ran right into the enemy's arms. The first things you see are heavens doors")
    print("GAME OVER")

def option_story_6():
    print("You decided to take a look. Bad idea. Snipers overlook the area. As soon you opened the door you met a bullet to your head.")
    print("GAME OVER")

def option_story_3():
    print("You decided to stay. You're trying to hide under the debries from your now demolished house. A bomb that exploded not too far from your position injured your leg quite badly. you won't be able to run. But you survived the bombing. Do want to WAIT or take a look outside to SEE if it's clear?")
    choice = input("WAIT or SEE")
    print("Choose WAIT or SEE")

    if choice == "WAIT":
        main_story_3()
    elif choice == "SEE":
        option_story_6()

# MIDDEN - main_story_4
def main_story_2():
    main_story_4()

# MIDDEN - main_story_2 + option_story_4
def option_story_2():
    print("You decided to make a run for the door. It's a heavy door, but you make it in time to shelter for the bombs. The bombings seem to have quiet down. Do want to WAIT or take a look outside to SEE if it's clear?")
    choice = input("WAIT or SEE")
    print("Choose WAIT or SEE")

    if choice == "WAIT":
        main_story_2()
    elif choice == "SEE":
        option_story_6()

# BEGIN - option_story_2 + option_story_3 + option_story_4
def main_story_1():
    print("Sitting in your house. Bombs falling around you like snow in a blizzard.\nsuddenly... BANG!\nA bomb fell right on top of your house. The entrance to the bomb shelter is completely blocked, but you know there's a back exit wich can be used as a emergency entrance.\nWhat do you do? Stay hiding and use the debries as protection, you take the chance and make a run for the emergency entrance or do you run into the open field were the other shelter is located?")
    choice = input("RUN or STAY or FIELD")
    print("Choose RUN or STAY or FIELD")

    if choice == "RUN":
        option_story_2()
    elif choice == "STAY":
        option_story_3()
    elif choice == "FIELD":
        option_story_4()

main_story_1()
