#Given an integer n, return True if n is within 10 of either 100 or 200

def r(n):
    if((abs(100-n)<=10) or (abs(200-n)<= 10)):
        print("n is within range")
    else:
        print('n is not in range')


r(98)