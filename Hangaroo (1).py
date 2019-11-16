import string
import random

wordsToGuess = ["hello", "halloween", "dog", "fish", "saints", "university", "butterfly",
            "silence", "lamb", "star"]

secretWord = random.choice (wordsToGuess)


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

def getAvailableLetters():
    lettersGuessed = input("Enter a list of letters: ")
    
    lowerCaseLetters = string.ascii_lowercase
    notInLettersGuessed = ''
    for i in lowerCaseLetters:
        if i not in lettersGuessed:
            notInLettersGuessed = notInLettersGuessed + i
    return notInLettersGuessed

def Hangaroo(secretWord):
    length = len(secretWord)
    lettersGuessed = []
    guessTheWord = False
    attempts = 5
    
    print ("Welcome to Hangaroo! guess the word correctly and you will be spared.")
    print ("\nHint:The word contains ", length, " letters.\n")
    
    
    while attempts > 0 and attempts <=5 and guessTheWord is False:
        if secretWord == getGuessedWord(secretWord, lettersGuessed):
            guessTheWord = True
            break
        
        print ("You have ", attempts, " attempts left.")
        print ("The available letters are: ", getAvailableLetters (lettersGuessed))
        word = str
        word = input ("Enter a letter: ").lower()
        
        if word in secretWord:
            if word in lettersGuessed:
                print ("This letter has been used. Try another letter.")
            else:
                    lettersGuessed.append(word)
                    print ("Great!")
                    print (getGuessedWord(secretWord,lettersGuessed))
        
        else:
            if word in lettersGuessed:
                print ("This letter has been used. Try another letter.")
            else:
                lettersGuessed.append(word)
                attempts = attempts - 1
                print ("The letter you entered is incorrect.")
    if guessTheWord == True:
        return "Congratulations! You suceeded."
    elif attempts == 0:
        print ("Unable to guess the word.")
        print ("The word was", secretWord, ".")
    
               