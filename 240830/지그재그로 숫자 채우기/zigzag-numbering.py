m,n = map(int,input().split())

arr_2d = [
    [0 for _ in range(n)]
    for _ in range(m)
]

num = 0
for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            arr_2d[j][i] = num
            num += 1
    else:
        for j in range(m - 1, -1, -1):
            arr_2d[j][i] = num
            num += 1

# 출력
for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()