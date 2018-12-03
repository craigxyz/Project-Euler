# Read file into list
with open("names.txt", "r") as f:
    for line in f.readlines():
        names = line.split(",")
names.sort()
total = 0
for i in range(len(names)):
#for name in names:
    sum = 0
    names[i] = names[i].strip('\"').lower()
    for letter in names[i]:
        sum += (ord(letter) - ord('a') + 1)
    #print("The name " + names[i] + " has a value of " + str(sum*(i+1)))
    total += (sum*(i+1))
print(total)
