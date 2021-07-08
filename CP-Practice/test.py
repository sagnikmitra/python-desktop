str1 = list(map(str, input()))
str2 = list(map(str, input()))
resStr = []
for i in range(len(str1)):
    if str1[i] not in str2:
        resStr.append(str1[i])
print(resStr)
