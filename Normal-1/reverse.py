x = -123
if x <0:
    sign=-1
else:
    sign=1
result=0
x=abs(x)
while x>0:
    digit=x%10
    result=result*10+digit
    x=x//10
if result<2**31 or result >2**31-1:
    print(0)
print(sign*result)
    