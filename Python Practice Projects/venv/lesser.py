#Write a function that returns the lesser of two given numbers if both numbers are even, but returns the
#greater if one or both numbers are odd

def lesser(x,y):
    if(x%2==0 and y%2==0):
        if(x<y):
            return x
        elif(y<x):
            return y
    else:
        if (x < y):
            return y
        elif (y < x):
            return x

#main intialization
result = lesser(77,11)
print(result)

