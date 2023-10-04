nums = []
x= str(input())
nums.extend(x)
val = str(input())
while val in nums:
    nums.remove(val)

print(len(nums))
for i in range(len(x)-len(nums)):
    nums.append('_')

print(nums)       