s="dhoni"
st=input()
v=list(set(s)-set(st))
va=list(set(st)-set(s))
v=len(v)+len(va)
if v==0:
	print("yes")
else:
	print("no")
