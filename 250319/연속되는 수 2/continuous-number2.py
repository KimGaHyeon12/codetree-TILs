n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
cnt = 0
cnt_arr = []
for i in range(n):
    if i == 0 or arr[i] == arr[i - 1]:
        cnt += 1
    else:
        cnt_arr.append(cnt+1)
        cnt=0

cnt_arr.append(cnt) #마지막 그룹은 반드시 별도로 추가해야 합니다.

if not cnt_arr:
    print(1)
else:
    print(max(cnt_arr))
