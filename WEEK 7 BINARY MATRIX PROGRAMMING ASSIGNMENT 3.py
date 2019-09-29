"""QUESTION
Given a matrix with N rows and M columns, the task is to check if the matrix is a Binary Matrix. A binary matrix is a matrix in which all the elements are either 0 or 1.

Input Format:
The first line of the input contains two integer number N and M which represents the number of rows and the number of columns respectively, separated by a space.
From the second line, take N lines input with each line containing M integer elements with each element separated by a space. 

Output Format:
Print 'YES' or 'NO' accordingly

Example:

Input:
3 3
1 0 0
0 0 1
1 1 0

Output:
YES

SOLUTION"""

n,m=map(int,input().split())
b=0
#UPLOADED BY ULTIMATE GAMER
for i in range(n):
    for j in range(1):
        temp=[int(g) for g in input().split()]
        for k in temp:
            if k!=0 and k!=1:
                b=b+1
                break
#UPLOADED BY ULTIMATE GAMER
if b==0:
    print("YES",end="")
else:
    print("NO",end="")
