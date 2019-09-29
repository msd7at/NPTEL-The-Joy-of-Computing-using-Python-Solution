"""QUESTION
You all have used the random library of python. You have seen in the screen-cast of how powerful it is.
In this assignment, you will sort a list let's say list_1 of numbers in increasing order using the random library.

Following are the steps to sort the numbers using the random library.

Step 1: Import the randint definition of the random library of python. Check this page if you want some help.

Step 2: Take the elements of the list_1 as input.

Step 3: randomly choose two indexes i and j within the range of the size of list_1.

Step 4: Swap the elements present at the indexes i and j. After doing this, check whether the list_1 is sorted or not.

Step 5: Repeat step 3 and 4 until the array is not sorted.

Input Format:
The first line contains a single number n which signifies the number of elements in the list_1.
From the second line, the elements of the list_1 are given with each number in a new line.

Output Format:
Print the elements of the list_1 in a single line with each element separated by a space. 
NOTE 1: There should not be any space after the last element.

Example:

Input:
4
3
1
2
5

Output:
1 2 3 5

Explanation: 
The first line of the input is 4. Which means that n is 4, or the number of elements in list_1 is 4. The elements of list_1 are 3, 1, 2, 5 in this order.
The sorted version of this list is 1 2 3 5, which is the output.

NOTE 2: There are many ways to sort the elements of a list. The purpose of this assignment is to show the power of randomness, and obviously it's fun.


SOLUTION """

from random import randint
n =int(input())
l =[]
for i in range(n):
    ip=int(input())
    l.append(ip)
S=True
u=sorted(l)
while(S):
    j=randint(0,n-1)
    i=randint(0,n-1)
    ab=l[j]
    l[j]=l[i]
    l[i]=ab
    if l==u:
      S=True
    else:
      S=False
      
    if(S):
        break
    else:
        S=True
for b in range(n):
    if(b==n-1):
        print(l[b],end="")
    else:
        print(l[b],end=" ")
