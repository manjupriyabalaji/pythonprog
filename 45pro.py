import sys, string, math

s = input()
if s == s[::-1] :
    print('yes')
    sys.exit()
b = 0
for cust in s[::-1] :
    if c == '0' :
        b += 1
    else :
        break
so = '0'*b + s

if so== so[::-1] :
    print('yes')
else :
    print('no')
