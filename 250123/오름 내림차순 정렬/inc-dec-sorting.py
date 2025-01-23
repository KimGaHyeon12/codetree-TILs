n = int(input())
nums = list(map(int, input().split()))

# Write your code here!
nn= sorted(nums)
rn = nn[::-1]

for _ in nn:
    print(_,'',end='')
print()
for _ in rn:
    print(_,'',end='')