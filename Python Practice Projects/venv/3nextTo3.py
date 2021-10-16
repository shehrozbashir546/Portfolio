#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def check(numb):
    for x in range(0,len(numb)-1):
        y=numb[x]
        z=numb[x+1]
        if(y==3 and z==3):
            print('True')
        else:
            pass


list = [1,3,2,2,1,3,3]
check(list)