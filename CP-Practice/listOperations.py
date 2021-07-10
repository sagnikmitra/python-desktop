n = int(input())
list1 = [list(map(str, input().split())) for i in range(n)]
listRes = []
for i in range(n):
    if(list1[i][0] == "insert"):
        listRes.insert(int(list1[i][1]), int(list1[i][2]))
    elif(list1[i][0] == "remove"):
        listRes.remove(int(list1[i][1]))
    elif(list1[i][0] == "append"):
        listRes.append(int(list1[i][1]))
    elif(list1[i][0] == "print"):
        print(listRes)
    elif(list1[i][0] == "sort"):
        listRes.sort()
    elif(list1[i][0] == "reverse"):
        listRes.sort(reverse=True)
    elif(list1[i][0] == "pop"):
        listRes.pop()
