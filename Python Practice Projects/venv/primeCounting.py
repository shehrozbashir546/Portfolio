#Write a function that returns the number of prime numbers that exist up to and including a given number

def primeC(num):
    # check for 0 or 1 input
    if num<2:
        return 0
    # 2 or greater

    # storing our primes
    primes = [2]
    # counter going up to the input num
    x = 3
    # x is going through every number up to input num
    while x<=num:
        # check if x is prime
        for y in primes:
            if x%y==0:
                x +=2
                break
        else:
            primes.append(x)
            x+=2
    print(primes)
    print(len(primes))

primeC(100000)