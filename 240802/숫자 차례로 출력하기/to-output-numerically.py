# 변수 선언 및 입력:
n = int(input())


def print_star(n):    # 1부터 n번째 줄까지 별을 출력하는 함수
    if n == 0:        # 종료 조건
        return

    print(str(n).' ',end='')    # n번째 줄에는 n개의 별을 출력합니다.
    print_star(n - 1) # 1부터 n - 1번째 줄까지 출력하는 함수

def print_star2(n):    # 1부터 n번째 줄까지 별을 출력하는 함수
    if n == 0:        # 종료 조건
        return

    print_star(n - 1) # 1부터 n - 1번째 줄까지 출력하는 함수

    print(str(n).' ',end='')    # n번째 줄에는 n개의 별을 출력합니다.
    


print_star2(n)
print()
print_star(n)