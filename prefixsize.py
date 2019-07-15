x = int(input())
strn1 = []
for y in range(0,x):
    strn = input()
    strn1.append(strn)

y = 0
z = 0
flag = True
for b in range(0,len(strn1[0])):
    if(flag==False):
        break
    s=1
    while(s<x and strn1[0][y]==strn1[s][y]):
        s+=1
    if(s==x):
        z+=1
    else:
        flag = False
        break
    
for y in range(0,z):
    print(strn1[0][y],end="")
