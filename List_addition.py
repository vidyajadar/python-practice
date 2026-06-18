L = [2,4,3,5,7]
Choice = int(input("Enter a number:"))

pairs=[]

for i in range(len(L)):
    temp = L[i]

    for j  in range(i+1,len(L)):
        if temp+L[j]==Choice:
            pairs.append((temp,L[j]))
print(pairs)