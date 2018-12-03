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

def arePrimePerm(num):
    digits = list(str(num))
    l = list(permutations(digits)) # list of arrays containing all combo of digits
    combos = [] # list to hold all permutations of num
    for permutation in l: 
        strNum = ''.join(permutation)
        if strNum not in combos: # to ensure no number is added twice due
            combos.append(int(strNum))
    # now combos is filled
    if (isPrime(num) and (num != 1487)):
        if (num + 3330) in combos:
            if isPrime(num+3330):
                if (num + 3330 + 3330) in combos:
                    if isPrime(num+3330+3330):

                        print(num)
                        print(num + 3330)
                        print(num + 3330 + 3330)
                        return True

for i in range(1000,3340):
    arePrimePerm(i)