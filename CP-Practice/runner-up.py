lenArr = int(input())
arr = list(map(int, input().split()))
arr.sort()
for i in range(len(arr)-2, -1, -1):
    if(arr[i] != arr[(len(arr)-1)]):
        print(arr[i])
        break
