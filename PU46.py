# proving Goldbach's other conjecture false
'''
def isPrime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                # Explains why a number is not prime:
                #print(i,"times",num//i,"is",num)
                return False
        else:
            return True
    else:
        return False

def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True
'''
def isSquare(num):
    if (num**(.5)).is_integer():
        return True
    else:
        return False

def createSieve(num):
    sieve = []
    for i in range(1,num+1):
        if isPrime(i):
            sieve.append(i)
    return sieve

primeList = createSieve(10000)
result = 1
notFound = True

while(notFound):
    result+=2

    j = 0
    notFound = False
    while (result >= primeList[j]):
        if isSquare((result-primeList[j])/2):
            notFound = True
            break
        j+=1
print(result)






