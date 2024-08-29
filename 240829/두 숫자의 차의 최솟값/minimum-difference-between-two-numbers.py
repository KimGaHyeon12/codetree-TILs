n = int(input())
arr = list(map(int, input().split()))

min_diff = 200  # Setting it to a value higher than the maximum possible difference

# Iterate through the list to find the minimum difference between consecutive elements
for i in range(1, n):
    cha = arr[i] - arr[i - 1]
    if cha < min_diff:
        min_diff = cha

print(min_diff)