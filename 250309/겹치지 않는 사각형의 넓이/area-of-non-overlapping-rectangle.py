x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
MAX = 2000
checked = [[0] * (MAX + 1) for _ in range(MAX + 1)]
#print(x1)  [1, 6, 2]

#체크 배열 업데이트
for i in range(2):
    for x in range(x1[i],x2[i]):
        for y in range(y1[i],y2[i]):
            checked[x+1000][y+1000] = 1

i=2
for x in range(x1[i],x2[i]):
    for y in range(y1[i],y2[i]):
        checked[x+1000][y+1000] = 0

cnt  = sum(1 for i in range(MAX + 1) for j in range(MAX + 1) if checked[i][j] in {1, 2})

print(cnt)