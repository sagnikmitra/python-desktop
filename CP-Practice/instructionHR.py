n = int(input())
s = set(map(int, input().split()))
m = int(input())
iL = [list(map(str, input().split())) for i in range(m)]
for i in range(len(iL)):
    if iL[i][0] != 'pop':
        iL[i][1] = int(iL[i][1])
for i in range(len(iL)):
    if iL[i][0] == 'pop':
        s.pop()
    if iL[i][0] == 'remove':
        s.remove(iL[i][1])
    if iL[i][0] == 'discard':
        s.discard(iL[i][1])
print(sum(list(s)))
