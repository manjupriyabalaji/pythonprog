try:
	man=int(input())
	a=list(map(int,input().split()))
	p=[]
	for i in array:
		if array.count(i)>1:
			if i not in p:
				p.append(i)
	print(*p)
	if len(p)==0:
		print("unique")
except ValueError:
	print("invalid")
