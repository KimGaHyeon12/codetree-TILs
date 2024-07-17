def  printStar(n):
    if n==0:
        return
    else: 
        print("HelloWorld")
        printStar(n-1)


N = int(input())
printStar(N )