arr = list(map(int, input()))
k = int(input())
count = 0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if(arr[i] <= arr[j] and (arr[j]+arr[i]) % k == 0):
            count += 1
print(count//2)
