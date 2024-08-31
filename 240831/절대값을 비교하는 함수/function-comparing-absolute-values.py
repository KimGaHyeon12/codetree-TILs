n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    if a <0:
        a= a*-1
    if b <0:
        b= b*-1
    if a>b:
        print(a)
    if b>=a:
        print(b)