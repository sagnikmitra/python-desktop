n = int(input())
# This is for taking the marksheet nested list input
marksheet = [list(map(str, input().split())) for i in range(n)]
# print(marksheet)
name = input()
for i in range(n):
    for j in range(1, 4):
        marksheet[i][j] = float(marksheet[i][j])
for i in range(n):
    if name in marksheet[i]:
        print("%.2f" % ((marksheet[i][1]+marksheet[i][2]+marksheet[i][3])/3))
        break
