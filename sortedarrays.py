mn1=int(input())
xyy1=[]
for i in range(mn1):
	k=input()
	k=list(map(int,k.split(" ")))
	z=len(k)
	for i in range(z):
		xyy1.append(k[i])
xyy1.sort()
print(*xyy1,sep=" ")
