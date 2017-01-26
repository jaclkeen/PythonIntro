from termcolor import colored

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
userAddedLetters = list()

def alphabits():
    # Python 2 is raw_input, Python 3 is input
    letterInput = raw_input("Please enter letter {0} of the alphabet: ".format(len(userAddedLetters) + 1)).lower()

    if letterInput == alphabet[len(userAddedLetters)]:
        userAddedLetters.append(letterInput)
        print colored("Correct", "green")

    elif len(letterInput) > 1:
        print(colored("Only one letter at a time", "red"))        

    else:
        print colored("Incorrect", "red")

while(len(userAddedLetters) < 26):
    alphabits()

print(colored("\n Congratulations, you win!", "green"))