a=int(input())
b=0
for c in range(0,a):
  if(pow(2,c)>a):
    break
  b=a-pow(2,c)
print(b)
