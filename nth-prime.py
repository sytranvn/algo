import sys
from math import floor , sqrt, log

prims = []

# how big is MAX if given n?
# https://primes.utm.edu/howmany.html
def getNthPrime(n):
    global prims
    if not prims:
        makePrims(n)

    return prims[n-1]

def makePrims(n):
    global prims
    MAX = int(n *( log(n) + log(log(n)))) if n > 5 else 13
    checks = [True] * MAX
    for i in range(2, MAX):
            if checks[i]:
                prims.append(i)
                x = 2 * i
                while x < MAX:
                    checks[x] = False
                    x = x + i

if __name__ == "__main__":
    print(getNthPrime(int(sys.argv[1])))
    print(prims)


