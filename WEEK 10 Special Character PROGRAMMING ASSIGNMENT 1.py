"""
QUESTION:-
Given a string S, check whether it contains any special character or not. Print 'YES' if it does else 'NO'.

Input Format:

The first line contains the string S

Output Format:

Print 'YES' or 'NO'

Example:

Input:
Hi$my*name

Output:
YES

SOLUTION"""

s=input()
spch=['[','@','_','!','#','$','%','^','&','*','(',')','<','>','?','/','\\','|','}','{','~',':',']']
#uploaded by ultimate gamer
for i in s:
    if i in spch:
        print("YES",end="")
        break
else:
  print("NO",end="")
