nums = [0,0,1,1,1,2,2,3,3,4]
k=0
a=[]
for i in nums:
    if i not in a:
        a.append(i)
        k+=1
for i in range(len(a)):
    nums[i]= a[i]
print(k)
print(a)