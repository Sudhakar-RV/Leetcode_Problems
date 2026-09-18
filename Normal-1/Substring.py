s= "abcabcbb"
max=0
for i in range(len(s)):
    a=[]
    for j in range(i,len(s)):
        if s[j] in a:
            break
        a.append(s[j])
    if len(a)>max:
        max=len(a)
print(max)
            