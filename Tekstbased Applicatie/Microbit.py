from microbit import *
import speech
import random







lengteWoordArray = 3


onderwerp = ["i", "you", "we"]
werkwoord = ["walk", "speak", "drink"]
rest = ["fast", "at school", "coffee"]


def sayTheWords1(word):
    print(word)
    speech.say(word, speed=120, pitch=100, throat=100, mouth=200)
    sleep(500)


def sayTheWords2():
    willekeurigGetal = random.randint(0, lengteWoordArray - 1)
    display.show(willekeurigGetal)
    sayTheWords1(onderwerp[willekeurigGetal])
    sayTheWords1(werkwoord[willekeurigGetal])
    sayTheWords1(rest[willekeurigGetal])
    
    
while True:
    if button_a.is_pressed():
        display.show(Image.NO)
        sayTheWords1("NO very not nice")
    elif button_b.is_pressed():
        display.show(Image.YES)
        sayTheWords1("YES very nice")
    elif accelerometer.was_gesture('shake'):
        sayTheWords2()
    else:
        display.show(Image.HEART)