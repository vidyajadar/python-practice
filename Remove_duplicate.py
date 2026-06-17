nums = [5,1,5,2,3,2,1,4]
n2=[]
for i in nums:
    if i not in n2:
        n2.append(i)

n2.sort()
print(n2)