nums = [1,2,3,2,4,2]
nums2 = []
j=len(nums)

for i in range (j):
   nums2.append(nums[j-1])
   j-=1
print(nums2)