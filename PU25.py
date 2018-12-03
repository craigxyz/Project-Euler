fib = [1,1]
curr = len(fib) - 1 # 1 at start
# while the length of fib at index 1 != 1000
while (len(str(fib[curr])) != 1000):
    fib.append(fib[curr] + fib[curr-1])
    curr = len(fib) - 1

else:
    print(len(fib))