Welcome!
This project contains everything needed for a full competitive-programming problem, similar to what you’d see on Codeforces.

The goal is to provide:

A completely original, not-found-anywhere-else problem

A clean problem statement

An optimal solution + an optional brute-force solution

Test cases

A test-case generator

And three failed attempts from the Qwen AI model

Notes explaining how the problem idea was developed

Everything is organized in a simple folder structure so you can easily run, test, or modify the problem.

## t's Inside
├── qwen/                 # Where Qwen model tests are stored
│   ├── conversations.md  # Links and notes from Qwen runs
│   ├── run_01.py         # Qwen attempt #1 (fails)
│   ├── run_02.py         # Qwen attempt #2 (fails)
│   └── run_03.py         # Qwen attempt #3 (fails)
│
├── test_cases/           # Sample tests with input/output files
│   ├── 1.in
│   ├── 1.out
│   └── ...
│
├── idea.md               # How the problem was created
├── problem.md            # The official problem statement
├── solution.md           # Explanation of how to solve it
├── solution.py           # Working, optimal Python solution
├── solution_bf.py        # Optional brute-force version
├── generator.py          # Optional program to generate random tests
│
├── requirements.json     # Time & memory limits
└── README.md             # This file

**Purpose Of The This Project**
This project is designed for three main uses:

1. Competitive Programming
You can treat this like a real Codeforces problem. It comes with:
a full solution
edge test cases
and a brute-force checker

2. AI Model Testing
There are three attempts from the Qwen3 AI model.
They are supposed to fail at least one test case each.
Their code and run links are saved under qwen/.

3. Learning & Reference
If you want to learn how to design competitive programming problems,
idea.md explains how the idea evolved
solution.md explains the logic behind the answer
 
 ###  Running Things

Run the main solution:

python3 solution.py < test_cases/1.in


Run the brute-force solution:

python3 solution_bf.py < test_cases/1.in


Generate more tests:

python3 generator.py
