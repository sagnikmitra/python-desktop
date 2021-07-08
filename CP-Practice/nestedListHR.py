n = int(input())
# This is for taking the marksheet nested list input
marksheet = [[input(), float(input())] for i in range(n)]
# For debugging the set: print(set([marks for name, marks in marksheet]))
# Calculating the second highest number by typecasting to a set to omit duplicates and later converting again to a list
second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a, b in sorted(marksheet) if b == second_highest]))
