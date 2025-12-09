# Brute-force: only works for small n
from math import gcd
from itertools import combinations

n = int(input())
a = list(map(int, input().split()))

res = 0
for l in range(1, n+1):
    for combo in combinations(a, l):
        res = max(res, gcd(*combo) * l)

print(res)
