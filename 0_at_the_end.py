L=[0,1,0,3,12]
count = L.count(0)
for _ in range(count):
    L.remove(0)
    L.append(0)
        
print(L)