s = "1337c0d3"
i=0
sign=1
num=0
while i <len(s) and s[i]==" ":
    i+=1
if i <len(s) and s[i]=="+":
    i+=1
elif i <len(s) and s[i]=="-":
    sign=-1
    i+=1
while i <len(s) and s[i].isdigit():
    num=num*10+ int(s[i])
    i+=1
num=num*sign
if num <-2**31:
    print (-2**31)
if num>2**31-1:
    print (2**31-1)
print(num)
    
    