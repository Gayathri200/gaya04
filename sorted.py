x=int(input())
m=map(int,input().split())
a=list(m)
s=len(a)
if(s==x):
  num=sorted(a)
  for i in range(0,s):
    print(num[i],end=" ")
