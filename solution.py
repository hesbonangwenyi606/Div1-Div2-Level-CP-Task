import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
maxA = 10**6 + 1
freq = [0]*maxA

for x in a:
    freq[x] += 1

res = 0
for g in range(1, maxA):
    count = 0
    for multiple in range(g, maxA, g):
        count += freq[multiple]
    res = max(res, count * g)

print(res)
