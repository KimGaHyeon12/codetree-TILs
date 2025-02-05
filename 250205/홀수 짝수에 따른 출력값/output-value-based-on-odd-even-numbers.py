N = int(input())

# Write your code here!

def f(n):
   if n<=0: 
    return 0
   else:
     #1부처 N 까지 홀수 더하기
    return n+ f(n-2)

print(f(N ))
   