n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
 ans,cnt = 0,0

 for i n range(n):
    if i>=1 and arr[i]>arr[i-1]:
        cnt+1
    else:
        cnt=1
    ans = max(ans,cnt)

print(ans)