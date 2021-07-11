queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        for i in range(0, 2*n+1, 2):
            print(i)
    else:
        for i in range(1, 2*n+1, 2):
            print(i)
