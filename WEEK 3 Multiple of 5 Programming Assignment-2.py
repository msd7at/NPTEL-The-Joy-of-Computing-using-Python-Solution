#SOLUTION

x=[int(i) for i in input().split()]
l=[]
for j in x:
    if j%5!=0:
        l.append(j)
for k in range(len(l)):
    if k!=len(l)-1:
        print(l[k],end=" ")
    else:
        print(l[k],end="")
