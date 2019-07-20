a3=int(input())
top3=list(map(int,input().split()))
cookiee1=1
sum1=0
if top3[0]>top3[1]:
    cookiee1=cookiee1+1
    sum1=sum1+sum1
else:
    sum1=sum1
for j in range(1,len(top3)):
    if top3[j]>top3[j-1]:
        cookiee1=cookiee1+1
        sum1=sum1+sum1
    else:
        cookiee1=1
        sum1=sum1+sum1
print(sum1)
