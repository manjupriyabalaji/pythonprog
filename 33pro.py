b=input()
fj=0
for i in range(0,len(b)-1):
  for j in range(i+1,len(b)):
    if b[i]<b[j]:
      fj=1
      print(b[j:])
      break
  if fj==1:
    break
else:
  print(b)
