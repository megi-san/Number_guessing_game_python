import random

def get_number(message):
    while True:
        try:
            value = int(input(message))
            return value
        except:
            print("Enter a digital number please.")


if __name__=="__main__":
    #Lower input 
    lower = get_number("Enter Lower bound: ")

    #Upper input
    test=True
    while test:
        upper = get_number("Enter Upper bound: ")
        test=not(upper>=lower)
        if lower>upper : print("The number must be higher than Lower bound.")

    x=random.randint(lower,upper)
    count = 0

    while True:
        guess=get_number("Guess a number: ")
        count+=1
        if x == guess:
            print("Congratulations you guessed it in ",count, " tries")
            break
        elif x > guess:
            print("You guessed too small!")
        elif x < guess:
            print("You Guessed too high!")