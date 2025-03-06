n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
answer = [[0]*202 for _ in range(202)]
for t in range(n):
    x1_ = x1[t]+101
    x2_ = x2[t]+101
    y1_ = y1[t]+101
    y2_ = y2[t]+101
    for i in range(x1_,x2_ ):
        for j in range(y1_,y2_ ):
            answer[i][j] = 1

#16+4
print(sum(sum(answer[i]) for i in range(202)))