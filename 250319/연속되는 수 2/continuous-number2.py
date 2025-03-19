n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
cnt = 0
cnt_arr = []
for i in range(n):
    if i == 0 or arr[i] == arr[i - 1]:
        cnt += 1
    else:
        cnt_arr.append(cnt)
        cnt=0


print(max(cnt_arr)+1)
