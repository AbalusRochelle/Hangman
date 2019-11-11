def hangman(secretWord):
    length=len(secretWord)
    print("Welcome to Hangman!")
    print("I am thinking of a word that is", length, "letters long.")
    life=4
    i=0
    lettersGuessed=[]
    while (life!=0):
        print("________________________________________________________________")
        if secretWord!= getGuessedWord(secretWord,lettersGuessed):
            print("You have", life, "guesses left.")
            print("Available letters: ", getAvailableLetters(lettersGuessed))
            guess=input("Please guess a letter: ")
            guessInLowerCase = guess.lower()
            
            if guessInLowerCase in lettersGuessed:
                print("Oops! You have already guessed that letter: ", getGuessedWord (secretWord, lettersGuessed))
                
            elif guessInLowerCase not in secretWord:
                print("Oh no! That letter is not in my word: ", getGuessedWord (secretWord, lettersGuessed))
                life-=1
            else:
                lettersGuessed.append(guessInLowerCase)
                print("Yeah!Good guess:",getGuessedWord(secretWord, lettersGuessed))
               
            lettersGuessed.append(guessInLowerCase)
        elif secretWord==getGuessedWord(secretWord, lettersGuessed):
            print ("Congratulations, you got it right!. The word was " + secretWord)
            break
        
    else:
        print("________________________________________________________________")
        print("Sorry, you ran out of guesses. The word was " + secretWord)
        