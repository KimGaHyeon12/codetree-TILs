N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.

cnt = 0

for i in range(N):
    if i==0 or arr[i] * arr[i - 1] < 0:
        cnt+=1

print(cnt+1)