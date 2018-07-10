import time
def robot():
    time.sleep(.5)
    print("Yo waddup, my name's Jared, I'm 17, and I never learned how to friggin read")

def whatever(answer):
    time.sleep(1)
    print("Dude, I can't even read")
    time.sleep(2.5)

def what(answer):
    if 'h' in answer:
        time.sleep(1)
        print("Yo waddup, my name's Jared, I'm 17, and I--")
        time.sleep(1.5)
        print("Wait, I already said that didn't I?")
        time.sleep(2)
    else:
        whatever(answer)

def hangman(answer):
    choose = input('Wanna play hangman? (Y/N?) ')
    choose = choose.lower()
    if 'y' in choose:
        time.sleep(1)
        print('Rite on then!')
        time.sleep(1)
        import hangman.py
    if 'n' in choose:
        time.sleep(2)
        print('Your loss, dude')
        time.sleep(2)
        exit()

def posthangman():
    time.sleep(2)
    print("That was far out, man")
    time.sleep(1)
    print("See ya l8r dude")
    exit()
# --- Put your main program below! ---
def mainfunc():
    robot()
    while True:
        time.sleep(2)
        answer = input("(What will you say?) ")
        what(answer)
        hangman(answer)
        posthangman()
    while False:
        exit()

mainfunc()
