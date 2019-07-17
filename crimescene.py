aaa=int(input())
bbb=list(map(int,input().split()))
ccc=0
for m in range(0,aaa):
	for p in range(0,m):
		if bbb[p]<bbb[m]:
			ccc=ccc+bbb[p]
print(ccc)
