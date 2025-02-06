n=int(input())
arr=list(map(int,input().split()))
ans=arr[0] # 첫 번 째 수로 초기화

def gcd(a,b): # 유클리드 호제법을 이용해 최대공약수 구하기
    if a<b: # a가 더 큰 수 
        a,b=b,a
    if b==0: # 종료조건
        return a
    return gcd(b,a%b) # 재귀호출

def lcm(a,b): # 최소 공배수 = 두수의 곱 / 두수의 최대 공약수
    return int(a*b/gcd(a,b))

for num in arr:
    ans=lcm(num,ans)

print(ans)