L1 = [1,2,3]
L2 = [6,5,4]
L3 = L1+L2 
print("Merged list",L3)

for i in range(len(L3)):
    for j in range (len(L3)-1):
        if L3[j]>L3[j+1]:
            temp = L3[j]
            L3[j] = L3[j+1]
            L3[j+1] = temp
print("Sorted list",L3)