def is_even(num):
    if num % 2 == 0:
        #print("%s is even" %(num))
        return True
    else:
        #print("%s is odd" %(num))
        return False

def mainfunc():
    num = int(input("Gimme an even number: "))
    print(is_even(num))
    exit()

mainfunc()
