# Random test generator
import random

n = 200000
a = [random.randint(1, 10**6) for _ in range(n)]
print(n)
print(' '.join(map(str, a)))
