a,b=map(int,input().split())
m=map(int,input().split())
h=list(m)
s=len(h)
if(s==a):
  for i in range(b,s):
    print(h[i],end=" ")
  for i in range(0,b):
    print(h[i],end=" ")  
