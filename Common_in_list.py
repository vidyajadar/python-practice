a =[1,2,3,4]
b =[2,4,6,8]
c = []
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b [j]:
            c.append(a[i])
print("Common in a and b list",c)