n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]


# Write your code here!

for q in queries:
    #for i in range()
    a,b = q
    new_arr = arr[a-1:b]
    print(sum(new_arr))