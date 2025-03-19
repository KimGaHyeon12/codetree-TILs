N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.

cnt = 0
cnt_arr = []
for i in range(1,N):
    if arr[i] * arr[i - 1] > 0:
        cnt+=1
    else:
        cnt_arr.append(cnt)
        cnt=0

cnt_arr.append(cnt)

if not cnt_arr:
    print(1)
else:
    print(max(cnt_arr) + 1)