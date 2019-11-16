def getGuessedWord():
    secretWord = input("Enter the secret word: ")
    lettersGuessed = input("Enter a list of letters: ")
    
    word = ''
    for i in secretWord:
        if i in lettersGuessed:
            word = word + i
        else:
            word = word + '_ '
    return word