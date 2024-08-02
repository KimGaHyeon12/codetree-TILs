def print_num1(n):
    if n <= 0:
        return
    print(n,' ',end='')
    print_num1(n-1)

def print_num2(n):
    if n <= 0:
        return
    print_num2(n-1)
    print(n,' ',end='')


n=int(input())
print_num1(n)
print_num2(n)