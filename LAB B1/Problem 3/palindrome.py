wrd = input("Escriba una palabra:")

wrd2 = wrd[::-1]

if wrd == wrd2:
  print("Esta palabra es un Palindromo")
else:
  print("Esta palabra no es un Palindromo")
