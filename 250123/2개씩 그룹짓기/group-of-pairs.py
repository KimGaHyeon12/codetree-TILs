n = int(input())
nums = list(map(int, input().split()))

# Write your code here!
nums_ = sorted(nums) 

max = 0
for i in range(n):
    temp = nums_[i]+ nums_[-(i+1)]
    if max<temp:
        max = temp

print(max)