# Solution

## Observations
- Maximum weight will be for some GCD `g` multiplied by the number of elements divisible by `g`.
- Count the frequency of each number and all multiples of numbers up to 10^6.
- Compute for each possible GCD the total number of elements divisible by it, then calculate weight = g * count.

## Steps
1. Build frequency array `freq[x] = count of x in a`.
2. For each possible GCD `g` from 1 to 10^6:
   - Count elements divisible by `g` using multiples sum.
   - Calculate weight = g * count.
3. Take the maximum.

## Complexity
- O(n + maxA * log(maxA)) using sieve-like method.
- Fits within constraints.
