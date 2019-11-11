def getAvailableLetters(lettersGuessed):
    string=""
    count=0
    s='abcdefghijklmnopqrstuvwxyz'
    for i in s:
        if i in lettersGuessed:
            count+=1
        else:
            string+=i
    return string