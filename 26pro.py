n = int(input())
l = list(map(int, input().split()))
max = 0
c = 0
a = l[0]
for i in range(0,n-1):
    if a < l[i+1]:
        c +=1
        a = l[i+1]
    else:
        if max(l[i+1:]) < a:
            a = l[i+1]
print(c+1)
