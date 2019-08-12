y=int(input())
n=map(int,input().split())
ab=list(n)
s=len(ab)
if(s==y):
  num=sorted(ab)
  for j in range(0,s):
    print(num[j],end=" ")
