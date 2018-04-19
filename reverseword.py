"""@package docstring
Reverse Word.

More details.
"""
def reverse(userInput):
	"""Documentation for a function.
    More details.
    """
    userInputArray = userInput.split(" ")
    wordResult = ""
    for i in range(1, len(userInputArray)+1):
    	"""The constructor."""
        wordResult += userInputArray[len(userInputArray)-i]
        if i < len(userInputArray):
        	wordResult += " "
    return wordResult

if __name__ == "__main__":
	userInput = input("Ingrese una oracion: ")
	print(reverse(userInput))
