def end_story_5():
    print("You decided to hop onto the train to Berlin. When you arrive to head straight to the embassy of Berlin. Here you get everything you for a good life in the German city.")
    print("This script has ended! If you want to try again, close and restart!")

def main_story_11():
    print("You decided to decline the offer and keep on moving. After a while of traveling you find yourseld at a train station. There's one train going to Amsterdam and another going to Berlin. Wich one do you take? AMSTERDAM or BERLIN?")
    if choice == "AMSTERDAM":
        option_story_11()
    elif choice == "BERLIN":
        end_story_5()

def option_story_12():
    print("You have decided to accept the offer and stay in that room. You were able to find a job thatt pays enough for you to stay permanently")
    print("This script has ended! If you want to try again, close and restart!")

def option_story_10():
    print("You decide to visit a local town in hope for help. Here you come across some nice people that are willing to help you. After they heard of the journey you passed they offer you a hotelroom where you can stay. At least until you find a job and pay the rent. Do you ACCEPT the offer or do you DECLINE?")
    choice = input("ACCEPT or DECLINE")
    print("Choose ACCEPT or DECLINE")

    if choice == "ACCEPT":
        option_story_12
    elif choice == "DECLINE":
        main_story_11
    

def option_story_8():
    print("You decided to take a break from walking and stay for the night. You're way behind your original plans.")
    option_story_10()

def end_story_4():
    print("You decided to skip this test. Now you're not able to get a stable job without being a official Dutch citizen. No stable job = No income. You ended up on the streets of Amsterdam and have nowhere to go.")
    print("This script has ended! If you want to try again, close and restart!")

def end_story_1():
    print("You decided to do the test. First time you failed, but the second time absolutely nailed it! Good job! With this test done you're a official Dutch citizen and you can get a stable job with a good income to buy a house and rebuild your life!")
    print("This script has ended! If you want to try again, close and restart!")
    

def option_story_11():
    print("You decided to travel further along to the Netherlands. But here you need to complete a test to be an official citizen. Do you want to do this TEST or SKIP it and hope for the best?")
    choice = input("TEST or SKIP")
    print("Choose TEST or SKIP")

    if choice == "TEST":
        end_story_1()
    elif choice == "SKIP":
        end_story_4()

def end_story_2():
    print("You decided to stay in belgium. Your travels ended in the city Brussels. Here it's difficult to buildup a new life. New language, New people. But you managed to get a intership with a company to buildup your experience. A stable job is right around the corner!")
    print("This script is finished! If you want to try again, close and restart!")

def main_story_10():
    print("You decided to get in the car with the nice man. You travel along the coast al the way to belgium. The nice man is traveling to the Netherlands. Do you stay here in BELGIUM or do you travel further into NETHERLANDS")
    choice = input("BELGIUM or NETHERLANDS")
    print("Choose BELGIUM or NETHERLANDS")

    if choice == "BELGIUM":
        end_story_2()
    elif choice == "NETHERLANDS":
        option_story_11()

def option_story_9():
    print("You decided to travel further along the coast through the night. After an hour of walking you come across a friendly man in car willing to bring you to your destination because he's on a roadtrip. Do you GETIN or DECLINE his offer?")
    choice = input("GETIN or DECLINE")
    print("Choose GETIN or DECLINE")

    if choice == "GETIN":
        main_story_10()
    elif choice == "DECLINE":
        option_story_10()

def main_story_6():
    print("You decided to travel further along the coast. Without stopping you already covered about 30 miles. But it's getting late. You can travel further or get some sleep during the night and travel again first thing in the morning.\nWhat do you do? TRAVEL or SLEEP?")
    choice = input("TRAVEL or SLEEP")
    print("Choose TRAVEL or SLEEP")

    if choice == "TRAVEL":
        option_story_9()
    elif choice == "SLEEP":
        option_story_8()

def end_story_3():
    print("You decided to stay. You got a job not too far from the camp. It's not the best, but it's enough to rebuild a life. You and you're family are happy again and don't have to listen to explosions going on in the distance.")
    print("You survided!")
    print("This script finished. If you want to try again, close and restart!")

def main_story_5():
    print("You decided to take the boat out of town. You now find yourself in a situation were there's no escape. Being attacked while at sea will be fatal. Luckily you arrive without much problems. You now find yourself in Greece.\nHere you have to choose. Go along the coast and keep on traveling or stay with this camp where you're safe at least from the bombing runs.\nWhat do you do? Travel along the COAST or STAY?")
    choice = input("COAST or STAY")
    print("Choose COAST or STAY")

    if choice == "COAST":
        main_story_6()
    elif choice == "STAY":
        end_story_3()

def option_story_5():
    print("You decided to wait. That evening another bombing of the area was planned. No one survived the second waves of bombs.")
    print("GAME OVER. If you want to try again, close and restart!")

def main_story_4():
    print("After a while of waiting you hear talking noices in the distance. You decide to check it out. When you arrive you see people in distress. You know to get out of the town as fast as possible, but you know the risk.\nThere's a boat leaving the country in 5 minutes. What do you do? Take the BOAT or STAY and wait what will happen next?")
    choice = input("BOAT or WAIT")
    print("Choose BOAT or WAIT")

    if choice == "BOAT":
        main_story_5()
    elif choice == "WAIT":
        option_story_5()

def main_story_3():
    main_story_4()

def option_story_4():
    print("You decided to run to an open field were you're hoping to be safe from the bombs. Bad luck! You ran right into the enemy's arms. The first things you see are heavens doors")
    print("GAME OVER. If you want to try again, close and restart!")

def option_story_6():
    print("You decided to take a look. Bad idea. Snipers overlook the area. As soon you opened the door you met a bullet to your head.")
    print("GAME OVER! If you want to try again, close and restart!")

def option_story_3():
    print("You decided to stay. You're trying to hide under the debries from your now demolished house, But you survived the bombing. Do want to WAIT or take a look outside to SEE if it's clear?")
    choice = input("WAIT or SEE")
    print("Choose WAIT or SEE")

    if choice == "WAIT":
        main_story_3()
    elif choice == "SEE":
        option_story_6()

def main_story_2():
    main_story_4()

def option_story_2():
    print("You decided to make a run for the door. It's a heavy door, but you make it in time to shelter for the bombs. The bombings seem to have quiet down. Do want to WAIT or take a look outside to SEE if it's clear?")
    choice = input("WAIT or SEE")
    print("Choose WAIT or SEE")

    if choice == "WAIT":
        main_story_2()
    elif choice == "SEE":
        option_story_6()

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

print("Welcome to my TekstBased Game! Here I tell a story with 2 or 3 choices. Answer these choices correctly and follow your path! Type START to begin")
choice = input()

if choice == "START":
    main_story_1()
