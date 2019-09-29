QUESTION
Programming Assignments-1: Addition
Due on 2019-08-14, 23:59 IST
In this assignment, you will have to take two numbers (integers) as input and print the addition.

Input Format:

The first line of the input contains two numbers separated by a space.

Output Format:

Print the addition in single line

Example:

Input:
4 2

Output:
6

Explanation:
Since the addition of numbers 4 and 2 is 6, hence the output is 6.

SOLUTION

a,b=input().split()
a=int(a)
b=int(b)
print(a+b,end="")
