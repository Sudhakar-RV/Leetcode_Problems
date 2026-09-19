a= [3,2,3]
freq={}
for i in a:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
    if freq[i]>len(a)//2:
        print(i)