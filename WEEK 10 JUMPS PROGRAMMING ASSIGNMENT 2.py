"""
QUESTION

One day Ajit got a strange feeling of jumping from one point to another. The jumping will be done in one ­dimension only. 
He will start from a point 0 and from there he will perform a lot of jumps. He can only jump in a specific sequence: 
1­jump, 2­jump, 3­jump, 1­jump, 2­jump, 3­jump, 1­jump, and so on. (1­>2­>3­>1­>2­>3­>1.....)

1-­jump means that if Ajit is at the point x, he will jump to the point x+1. 
2­-jumps mean that if Ajit is at the point x, he will jump to the point x+2. 
3­-jumps mean that if Ajit is at the point x, he will jump to the point x+3. 

Before the start Ajit asks you: will he arrive at the point a after some number of jumps?

Input Format:
The first line contains a single number a denoting the point Ajit asks about.

Output Format:
Output "YES" without a quotes if Ajit can arrive at point a or "NO" without quotes 
otherwise.

Example-1:

Input:
0

Output:
YES

Explanation:
He started at point 0

Example-2:

Input:
2

Output:
NO

Explanation:
From 0 he can take 1 jump to reach point 1 but after that  he can take only 2 jumps which will lead him to point 3.
Jump sequence (1­>2).

NOTE: The value of a can be as large as 1018. Please make your program efficient or you may receive run time error.
 SOLUTION """
 
ip=int(input())
x=ip%6
if x==0 or x==1 or x==3:
  print("YES",end="")
else:
  print("NO",end="")
