num = 0
for i in range(1,1001):
    num += i**i
lenNum = len(str(num))
for i in range(lenNum-10,lenNum):
    print(str(num)[i])