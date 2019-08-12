x=int(input())
m=map(int,input().split())
a=list(m)
s=len(a)
if(s==x):
  num=sorted(a)
  d=(s+1)//2
  print(num[d-1])
