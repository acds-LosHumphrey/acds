import random
import string

numberAnswer = ''.join([random.choice(string.digits) for n in range(4)])
cows, bulls = [0, 0]

if __name__ == "__main__":
    print("Pista: ", numberAnswer)
    while cows < 4:
        numberInput = [n for n in input("Ingresa un número de 4 dígitos: ")]
        numberInputClean = numberInput[:4]
        cows, bulls = [0, 0]
        for n in range(4):
            if numberAnswer[n] == numberInputClean[n]:
                cows += 1
        for i in numberInputClean:
            if i in numberAnswer:
                bulls += 1
        print("Cows: ",cows," Bulls: ",bulls-cows)
        if cows >= 4:
            print("Número adivinado! Respuesta: ", numberAnswer)