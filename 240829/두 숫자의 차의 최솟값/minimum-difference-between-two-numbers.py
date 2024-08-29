N = int(input())
arr =   list(map(int,input().split()))
 

min_ = 200
for i in range(1,5):
        cha = arr[i] - arr[i-1]
        if cha>0 and cha<min_:
            min_=cha

print(min_)