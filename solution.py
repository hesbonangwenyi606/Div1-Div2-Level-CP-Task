hesbonangwenyi@hesbonangwenyi-HP-ProBook-430-G5:~/Downloads/subsequence_weight_maximization$ for i in {1..5}; do     echo "Running test case $i:"                    # Prints which test case is running
    python3 solution.py < test_cases/$i.in | diff - test_cases/$i.out         && echo "OK"         || echo "FAIL"; done
Running test case 1:
1c1
< 9
---
> 12
FAIL
Running test case 2:
OK
Running test case 3:
OK
Running test case 4:
OK
Running test case 5:
OK
hesbonangwenyi@hesbonangwenyi-HP-ProBook-430-G5:~/Downloads/subsequence_weight_maximization$ 