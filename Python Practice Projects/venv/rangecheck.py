#Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    if num > low & num < high:
        print(f' {num} is in the range of {low} and {high}')
    else:
        print(f'{num} is not in the range')



ran_check(20,1,10)
