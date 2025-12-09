import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

maxA = 10**6 + 1
freq = [0] * maxA

# Step 1: count frequency of each number
for x in a:
    freq[x] += 1

res = 0
# Step 2: iterate from largest g to smallest
for g in range(maxA-1, 0, -1):
    count = 0
    # sum counts of all multiples of g
    for multiple in range(g, maxA, g):
        count += freq[multiple]
    # Step 3: calculate weight
    res = max(res, count * g)

print(res)
