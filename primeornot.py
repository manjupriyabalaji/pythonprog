s=int(input())
if s > 1:
    for x in range(2,s):
        if(s%x==0):
            print('no')
            break
    else:
            print('yes')
else:
            print('no')
