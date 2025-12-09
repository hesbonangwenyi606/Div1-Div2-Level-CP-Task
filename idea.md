# Idea Development

## Initial Concept
I wanted a problem that combines number theory and combinatorics. Using GCD over subsequences creates interesting optimization challenges because brute-force is too slow for large arrays.

## Rejected Variants
- Using sum instead of length * GCD: too easy; maximum is always the sum.
- Restricting to contiguous subarrays: too standard and predictable.

## Final Formulation
- Use subsequences instead of subarrays to make the problem non-trivial.
- Weight = length * GCD adds the optimization dimension.
- Constraints chosen so that naive brute-force fails (O(2^n)) and a smart solution using counting multiples or DP is needed.
