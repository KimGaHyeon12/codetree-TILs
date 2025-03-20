n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
distance_remember = -999999
count=0
answer = []
for i in range(1,n):
    
    if arr[i-2] + arr[i-1] == arr[i]:
        count +=1
    else:
        answer.append(count)
        count=0

answer.append(count)

if not answer:
    print(1)
else:
    print(max(answer)+2)
#print(answer)