x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.

empty = [[0]*2002 for _ in range(2002)] #-1000

for a in range(x1[0]+1000, x2[0]+1000):
    for b in range(y1[0]+1000, y2[0]+1000):
        empty[a][b]=1

for a in range(x1[1]+1000, x2[1]+1000):
    for b in range(y1[1]+1000, y2[1]+1000):
        empty[a][b]=0

x_arr = []
y_arr = []
for i in range(2001):
    for j in range(2001):
        if empty[i][j]==1:
            x_arr.append(i)
            y_arr.append(j)

if not x_arr or not y_arr:
    print(0)
else:
    x_len = max(x_arr) - min(x_arr)  + 1
    y_len = max(y_arr) - min(y_arr) + 1
    answer = x_len * y_len
    print(answer)

#print(x_arr)
#print(y_arr)

#print(max(x_arr),  min(x_arr)  , x_len)
#print(max(y_arr),  min(y_arr)  , y_len)

