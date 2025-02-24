n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]
arr = [0 for _ in range(n)]
# Write your code here!
for c in commands:
    start = c[0]
    end = c[1]
    for _ in range(start-1,end):
        arr[_] +=1
    #print(arr)
#print(arr)
print(max(arr))
 