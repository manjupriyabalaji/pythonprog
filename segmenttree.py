m1,n1 = map(int,input().split())
a1 = []
b21 = []
a1 = input().split()
for j in range(len(a1)):
    a1[j] = int(a1[j])
for j in range(n1):
    x,y = map(int,input().split())
    res = 0
    for j in range(x-1,y):
        res += a1[j]
    print(res)
