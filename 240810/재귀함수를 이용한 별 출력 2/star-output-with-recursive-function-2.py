def print_star1(n):
    if n == 0 :
        return
    for i in range(n):
        print("* ",end='')
    print()

    print_star1(n-1)

    for i in range(n):
        print("* ",end='')
    print()
 


 


N = int( input() )
print_star1(N)