"""@package docstring
Reverse Word.

Receives as a paramenter one sentence. As a result, it prints the sentence in a reverse order.
"""
def reverse(userInput):
	"""Function Reverse.
	Receives userInput as a sentence
    """
    userInputArray = userInput.split(" ")
    wordResult = ""
    for i in range(1, len(userInputArray)+1):
    	"""Iterator to go over the sentence and put it backwards"""
        wordResult += userInputArray[len(userInputArray)-i]
        if i < len(userInputArray):
        	wordResult += " "
    return wordResult

if __name__ == "__main__":
	userInput = input("Ingrese una oracion: ")
	print(reverse(userInput))
