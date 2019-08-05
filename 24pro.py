b=int(input())
m=2**b
z=[]
for i in range(0,p):
    l=bin(i)[2:].zfill(b)
    if(len(lt)<len(bin(2**b-1)[2:])):
        z.append([l.count("1"),l])
    else:
        z.append([l.count("1"),l])
z.sort()
for i in range(len(z)):
    print(z[i][1])
