n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Write your code here!
#print(segments)
arr = [0 for _ in range(200)]
for seg in segments:
    start = seg[0] +100
    end = seg[1] +100
    for i in range(start,end):
        arr[i] = arr[i] + 1
    #print(seg)
    #print(arr[:100])
    #print(arr[100:])   

print(max(arr))
#print("count", count)
#print(arr[:100])
#print(arr[100:])
