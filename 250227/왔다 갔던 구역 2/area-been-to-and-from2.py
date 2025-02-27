n = int(input())
x = []
dir =  []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
answer_arr  = [0] * 202
current = 0

for i in range(n):
    x1 =x[i]

    diract = dir[i]
    if diract=="L":
        x1= -1 * x1

    
    future = x1+current
    #print(x1, current, future)
    current_100 = current +100
    future_100 = future + 100
    #print(len(answer_arr),min(current,future), max(current,future) )
    for j in range(min(current,future), max(current,future)):
        answer_arr[j] +=1   

    count=0
    for a  in answer_arr:
        if a>1:
            count+=1

    current = future
print(count)