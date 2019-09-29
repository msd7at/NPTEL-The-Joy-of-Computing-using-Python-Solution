""QUESTION:

Given two numbers (integers) as input, print the smaller number.

Input Format:
The first line of input contains two numbers separated by a space

Output Format:
Print the smaller number

Example:

Input:
2 3

Output:
2
Private Test cases used for evaluation	Input	Expected Output	Actual Output	Status
Test Case 1	
100 10
 10
10
Passed
Test Case 2	
0 1
 0
0
Passed
Test Case 3	
10 9
 9
9
Passed
Test Case 4	
9 6
 6
6
Passed

Due Date Exceeded.
4 out of 4 tests passed.
You scored 100.0/100.

ANSWER ""

a,b=input().split()
a=int(a)
b=int(b)
if a > b:
  print(b,end="")
if a < b:
  print(a,end="")
