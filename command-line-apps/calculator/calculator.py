import math

def modifyInput(count):
    inputCount = "[{0}]>".format(count)
    letterInput = raw_input(inputCount + " Please enter a math expression: ")
    letterInput = letterInput.split(" ")
    letterInput = " ".join(letterInput)

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
    try:
        return eval(letterInput)
    except:
        return "Invalid equation"

execute()