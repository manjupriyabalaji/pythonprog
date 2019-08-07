b,s = map(int,input().split())
c=0
l = []
for i in range(b):
      l.append(input())
for i in range(b):
      for j in range(s-1):
            if l[i][j] != 'R' and l[i][j+1] != 'R' :
                  c+=3
            elif l[i][j] != 'G' and l[i][j+1] != 'G':
                  c+=5
print(c)
