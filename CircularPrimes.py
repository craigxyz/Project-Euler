from itertools import permutations

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

def isCircular(num): # 197
    strNum = str(num) 
    fam = [num]
    for _ in range(len(strNum)-1):
        strNum = strNum[1:] + strNum[0]
        child = int(strNum) 
        if child in fam:
            break

        fam.append(child)

    for child in fam:
        if (isPrime(child) == False):
            return False
    return True

count = 0
for i in range(0,1000000):
    if isCircular(i):
        print(i)
        count+=1
print("Number of circular primes below: " + str(count))
#print(isCircular(197))
'''
    digits = []
    maxIndex = len(str(num)) # 3 for 100
    
    for i in range(0,maxIndex):
        digits.append(str(num)[i])
    l = list(permutations(digits))
    combos = []
    for permutation in l:
        strNum = ""
        for j in range(0,len(permutation)):
            strNum += str(permutation[j])
        if strNum not in combos:
            combos.append(int(strNum))

    for each in combos:
       
        if not isPrime(each):
            return False
    return True
#print(isPrime(917))
#print(isCircular(197))

count = 0
for i in range(0,10000):
    if isCircular(i):
        print(i)
        count+=1
print("Number of circular primes below: " + str(count))
'''
