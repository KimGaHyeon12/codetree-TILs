N = int(input())

# Write your code here!

count = 0
def f(n,count):
    if n ==1:
        return count

    count+=1
    if n % 2 == 0:   #짝수면 2로 나눈 몫
        return f(n // 2, count)
    else:                     #홀수면 3로 나눈 몫
        return f(n // 3, count)  


print(f(N, count))
 
 