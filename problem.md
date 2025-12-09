# Problem: Subsequence Weight Maximization

You are given an array of $n$ positive integers $a_1, a_2, ..., a_n$. Define the **weight** of a subsequence $s$ as:

$$
\text{weight}(s) = (\text{length of } s) \times (\text{gcd of elements in } s)
$$

Your task is to find the **maximum possible weight** among all non-empty subsequences of the array.

### Input

- The first line contains a single integer $n$ ($1 \le n \le 2 \cdot 10^5$) — the size of the array.
- The second line contains $n$ integers $a_1, a_2, ..., a_n$ ($1 \le a_i \le 10^6$) — the elements of the array.

### Output

- Output a single integer — the maximum possible weight.

### Example

**Input**
```
5
2 4 6 3 9
```

**Output**
```
12
```
