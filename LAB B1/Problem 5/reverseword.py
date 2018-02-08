def reverse(userInput):
    userInputArray = userInput.split(" ")
    wordResult = ""
    for i in range(1, len(userInputArray)+1):
        wordResult += userInputArray[len(userInputArray)-i]
        if i < len(userInputArray):
        	wordResult += " "
    return wordResult

if __name__ == "__main__":
	userInput = input("Ingrese una oracion: ")
	print(reverse(userInput))
