#Given a string, return a string where for every character in the original there are three characters

def extendd(text):
    result = ''

    for char in text:
        result += char*3
    print(result)
    
extendd('Hello')