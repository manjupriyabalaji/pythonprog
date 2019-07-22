ms1=input()
x=list(map(int,ms1.split()))
y=x[1]
uv=input()
flag=0
ab=list(map(int,uv.split()))
for j in range(0,len(ab)-1):
	for k in range(j+1,len(ab)):
		if ab[j]+ab[k]==y:
			print("yes")
			flag=1
			break
	if flag==1:
		break
if flag!=1:
	print("no")
