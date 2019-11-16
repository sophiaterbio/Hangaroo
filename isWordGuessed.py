def isWordGuessed():
    secretWord = input("Enter the secret word: ")
    lettersGuessed = input("Enter a list of letters: ")
    
    word = 0
    for i in secretWord:
        if i in lettersGuessed:
            word = word + 1
        else:
            return False
    return True