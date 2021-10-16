#Write a function takes a two-word string and returns True if both words begin with same letter

def twoWord(text):
    wordlist = text.lower().split()
    print(wordlist)

    first = wordlist[0]
    second = wordlist[1]

    if(first[0] == second[0]):
        print('True')
    else:
        print('False')
    #main initialization

twoWord('Hello bHarry')
