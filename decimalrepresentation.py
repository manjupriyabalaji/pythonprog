mss=int(input())
x1=list(map(int,input().split()))
x1=[bin(j) for j in x1]
x1.sort(reverse=True)
x1=[int(p,2) for p in x1]
for j in range(0,mss):
 print(x1[j])
