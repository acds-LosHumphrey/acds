import random
import string

numberAnswer = ''.join([random.choice(string.digits) for n in range(4)])

def evaluateWord(word):
    cowsBulls = [0, 0]  #Cows posicion 0, Bulls posicion 1
    for n in range(4):
        if numberAnswer[n] == word[n]:
            cowsBulls[0] += 1
    for i in word:
        if i in numberAnswer:
            cowsBulls[1] += 1
    return cowsBulls

def defineAnswerManually(answer):
    global numberAnswer
    numberAnswer = answer

def play():
    cowsBulls = [0, 0]  #Cows posicion 0, Bulls posicion 1
    print("Pista: ", numberAnswer)
    while cowsBulls[0] < 4:
        numberInput = [n for n in input("Ingresa un numero de 4 digitos: ")]
        numberInputClean = numberInput[:4]
        cowsBulls = evaluateWord(numberInputClean)
        print("Cows: ",cowsBulls[0]," Bulls: ",cowsBulls[1]-cowsBulls[0])
        if cowsBulls[0] >= 4:
            print("Numero adivinado! Respuesta: ", numberAnswer)

if __name__ == "__main__":
    #defineAnswerManually("1234")
    play()
    