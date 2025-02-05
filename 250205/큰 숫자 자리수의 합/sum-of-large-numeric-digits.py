a, b, c = map(int, input().split())

# Write your code here!

 


# n의 각 자릿수의 합을 반환합니다.
def digit_sum(n):
    if n < 10:
        return n

    return digit_sum(n // 10) + n % 10


print(digit_sum(a * b * c))
