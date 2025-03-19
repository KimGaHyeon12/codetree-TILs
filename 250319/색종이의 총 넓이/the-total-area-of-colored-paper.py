n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
empty = [[0]*210 for _ in range(210)]


for p in points:
    x_start = p[0]
    y_start = p[1]
    for a in range(x_start+100,x_start+108 ):
        for b in range(y_start+100,y_start+108 ):
            empty[a][b]=1

answer = sum(sum(row) for row in empty)

print(answer)