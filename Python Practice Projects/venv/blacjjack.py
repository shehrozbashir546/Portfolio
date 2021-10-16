#Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'


def black(x,y,z):
    if sum([x,y,z]) <= 21:
        print(sum([x,y,z]))
    elif 11 in [x,y,z] and sum([x,y,z]) > 21:
        new = sum([x,y,z]) -10
        print(new)
    else:
        print('BUST')



black(2,11,10)