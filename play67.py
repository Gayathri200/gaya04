m,n=map(int,input().split())
x=map(int,input().split())
a=list(x)
s=len(a)
if(s==m):
  c=m-n
  for i in range(0,c):
    print(a[i],end=" ")
