# 변수 선언 및 입력:
n = int(input())


# a가 3n + 1 수열을 총 몇번 반복해야 1이 되는지 반환합니다.
def count_number(a):
    if a == 1:
        return 0

    if a % 2 == 0:
        return count_number(a // 2) + 1
    else:
        return count_number(3 * a + 1) + 1


print(count_number(n))
