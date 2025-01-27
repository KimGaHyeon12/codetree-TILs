N = int(input())

# Write your code here!

def fact(n):
    if n ==1:
        return n 

    return fact(n-1)+n

print(fact(N ))