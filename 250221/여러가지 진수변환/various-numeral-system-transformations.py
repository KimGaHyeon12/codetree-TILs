n , nanum = map(int,input().split())
digits = []

while True:
    if n < nanum:
        digits.append(n)
        break

    digits.append(n % nanum)
    n //= nanum

# print binary number
for digit in digits[::-1]:
    print(digit, end="")
