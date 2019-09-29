"""VIDEO LINK:- https://youtu.be/eVrBKWhXix8
QUESTION:-
Given a square matrix, you have to write a program to print it in a counter-clockwise spiral form.


Input Format:
The first line of the input contains an integer number n which represents the number of rows and columns in the matrix.
From the second line contains n rows with each row having n elements separated by a space.

Output Format:
Print the elements in a single line with each element separated by a space

Example:

Input:
4
25 1 29 7
24 20 4 32
16 38 29 1
48 25 21 19

Output:
25 24 16 48 25 21 19 1 32 7 29 1 20 38 29 4

Explanation: 
In the above example, each row, first all the elements of the first column is printed which are 25 24 16 48 after that, remaining elements of the last row is printed which are 25 21 and 19.
After which the remaining elements of the last column is printed which are 1 32 and 7 and so on...

ANSWER:-"""

a = int(input())
mat=[]

for i in range(0,a):    
    l = list(map(int, input ().split ()))
    mat.append(l)
m=a
n=a
k = 0
l = 0 
count = 0 
total = a*a
  
while (k < m and l < n) : 
    if (count == total) : 
        break
  
    for i in range(k, m) : 
        print(mat[i][l], end = " ") 
        count += 1
          
    l += 1
  
    if (count == total) : 
        break
         
    for i in range (l, n) : 
        print( mat[m - 1][i], end = " ") 
        count += 1
          
    m -= 1
          
    if (count == total) : 
        break
   
    if (k < m) : 
        for i in range(m - 1, k - 1, -1) : 
            print(mat[i][n - 1], end = " ") 
            count += 1
    n -= 1
  
    if (count == total) : 
        break
           
    if (l < n) : 
        for i in range(n - 1, l - 1, -1) : 
            print( mat[k][i], end = " ") 
            count += 1
                  
    k += 1
