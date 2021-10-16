#Write a function that capitalizes the first and fourth letters of a name

def cap(y):

    firstLetter = y[0]
    inbetween = y[1:3]
    fourthLetter = y[3]
    rest = y[4:]

    x= firstLetter.upper()+inbetween+fourthLetter.upper()+rest
    print(x)

cap('shehroz')