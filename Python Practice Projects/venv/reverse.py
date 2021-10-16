# return a sentence with the words reversed

def yoda(sentence):
    words = sentence.split()
    reversedWords = words[::-1]
    print(reversedWords)
    print("Now to join the list into a single string: ")
    final = ' '.join(reversedWords)
    print(final)

yoda('I am eating food and I am sittin at home')