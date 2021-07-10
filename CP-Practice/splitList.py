def merge_the_tools(string, k):
    list1 = []
    for i in string:
        list1.append(i)
    splitLen = int(len(list1)/k)
    splitList = [[] for i in range(splitLen)]
    # splitList = []
    for i in range(splitLen):
        for j in range(splitLen):
            splitList[i].append(list1[i*splitLen+j])
    for i in range(splitLen):
        print(splitList[i])
        splitList[i] = list(dict.fromkeys(splitList[i]))
        print(splitList[i])
        str1 = ""
        for j in range(len(splitList[i])):
            str1 += str(splitList[i][j])
        print(str1)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
