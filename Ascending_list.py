L=[5,1,2,3,4]
for i in range(len(L)):
    for j in range(len(L)-1):
        if L[j]>L[j+1]:
            temp = L[j]
            L[j] = L[j+1]
            L[j+1] =temp
        
    
print(L)