st1,st2=map(str,input().split())
b=0
if len(st1)>len(st2):
   st1,st2=st2,st1
c=0
while c<len(st1):
   c+=(ord(st2[c])-ord(st1[c]))
   c+=1
for c in range(c,len(st2)):
   b+=ord(st2[c])-ord('b')+1
print(b)
