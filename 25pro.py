n=int(input())
l=input().split()
s=[]
for i in range(n):
    g=lap[i]
    for j in range(i+1,n):
        if(int(lap[i])<int(lap[j]))and (int(lap[j-1])<int(lap[j])):
            g+=lap[j]
        else:
            break
    s.append(len(g))
print(max(s))
