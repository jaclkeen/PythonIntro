import math

def modifyInput(count):
    inputCount = "[{0}]>".format(count)
    letterInput = raw_input(inputCount + " Please enter a math expression: ")
    letterInput = " ".join(letterInput).split(" ")
    letterInput = filter(None, letterInput)

    return letterInput

def execute():
    count, lastAnswer, lastCommand = 0, 0, list()
    while(True):
        letterInput = modifyInput(count)
        if "".join(letterInput) == "exit" or "".join(letterInput) == "quit":
            break;
        elif "".join(letterInput) == "last":
            print lastAnswer
        elif "".join(letterInput) == "lastq":
            print " ".join(lastCommand)
        else:
            print formulaResult(letterInput)
            lastAnswer = formulaResult(letterInput)
            lastCommand = letterInput
            count += 1

def formulaResult(letterInput):
    if (len(letterInput) < 3):
        return "You must enter two letters and a math symbol"
    elif(letterInput[1] == '+'):
        return float(letterInput[0]) + float(letterInput[2])
    elif(letterInput[1] == '-'):
        return float(letterInput[0]) - float(letterInput[2])
    elif(letterInput[1] == '/'):
        return float(letterInput[0]) / float(letterInput[2])
    elif(letterInput[1] == '*'):
        return float(letterInput[0]) * float(letterInput[2])
    else:
        return "You entered an invalid equation"

execute()