xyz,cd=map(int,input().split())
i1=[]
for _ in range(xyz):
    i1.append(input())
for j in range(len(i1)):
    if('0' in i1[j]):
        i1[j]=i1[j].replace('0','')
    i1[j]=i1[j].replace(' ','')
lengths=[]
for j in i1:
    if(len(j)>0):
        lengths.append(len(j))
cd=min(lengths)
s1='1 '*cd
s1=s1.strip()
for j in range(cd):
    print(s1)
