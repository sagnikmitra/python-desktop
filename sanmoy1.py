
array = []
b = 0
c = int(input("Type the large number of your series"))
s = int(input("How many numbers you want to check"))
print("Type the numbers you want to check\n")
for i in range(0, s):
    n = int(input())
    array.append(int(n))
for i in range(1, c+1):
    for j in range(0, s):
        if(array[j] == i):
            b += 1
        if (b >= 2):
            print(f"Duplicate {i} :({b}) times\n")
        if (b == 0):
            print(f"{i} is missing.\n")
        b = 0
