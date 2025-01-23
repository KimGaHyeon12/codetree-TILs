n, k = map(int, input().split())
nums = list(map(int, input().split()))

# Write your code here!
nn = sorted(nums)
print(nn[k-1])