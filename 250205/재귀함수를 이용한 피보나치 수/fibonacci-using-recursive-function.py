N = int(input())

# Write your code here!

def f(n):
    # 종료 조건
    if n == 1:
        return 1
    if n == 2:
        return 1

    # 점화식
    return f(n - 1) + f(n - 2)


print(f(N))

 


