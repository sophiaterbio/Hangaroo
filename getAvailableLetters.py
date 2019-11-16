def getAvailableLetters():
    lettersGuessed = input("Enter a list of letters: ")
    
    import string
    lowerCaseLetters = string.ascii_lowercase
    notInLettersGuessed = ''
    for i in lowerCaseLetters:
        if i not in lettersGuessed:
            notInLettersGuessed = notInLettersGuessed + i
    return notInLettersGuessed