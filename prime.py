import time
def isPrime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                # Explains why a number is not prime:
                # print(i,"times",num//i,"is",num)
                return False
        else:
            return True
    else:
        return False

def nthPrime(num):
    start = time.time()
    count = 0
    n = 2
    while(count != num):
        if isPrime(n):
            count+=1
            n+=1
        else:
            n+=1
    else:
        print("The " + str(num) + "th prime is " + str(n-1))
        print("Elapsed time: " + str(round(time.time() - start,2)) + " sec.")

nthPrime(10001)