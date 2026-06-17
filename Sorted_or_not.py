L = [4,2,3,4,5]
is_sorted=True
for i in range(len(L)-1):
    if L[i]>L[i+1]:
        is_sorted = False
        break
print(is_sorted)