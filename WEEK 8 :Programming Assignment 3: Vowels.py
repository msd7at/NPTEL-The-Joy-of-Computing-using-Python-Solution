""

Given a string S of lowercase letters, remove consecutive vowels from S. After removing, the order of the list should be maintained.

Input Format:

Sentence S in a single line

Output Format:
Print S after removing consecutive vowels

Example:

Input:
your article is in queue

Output:
yor article is in qu

Explanation:

In the first word, 'o' and 'u' are appearing together, hence the second letter 'u' is removed. In the fifth word, 'u', 'e', 'u' and 'e' are appearing together, hence 'e', 'u', 'e' are removed.
""


#SOLUTION:-
def vow(l): 
  
    return ((l == 'a') or (l == 'e') or (l == 'i') or (l == 'o') or (l == 'u')) 
def final(ip): 
    print(ip[0], end = ""); 
    for i in range(1,len(ip)):
        if ((vow(ip[i - 1]) != True) or 
            (vow(ip[i])!= True)):          
            print(ip[i], end = "")
ip=input() 
final(ip)
