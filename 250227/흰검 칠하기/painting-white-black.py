n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
# Please write your code here.
answer_arr  = [""] * 202
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

    ###############다음 부분을 고쳐야 한다. 
    for j in range(min(current,future), max(current,future)):
        if diract=="L":
            if answer_arr[j]=="G":
                continue
            elif answer_arr[j]=="B":
                answer_arr[j] ="G"
            else:
                answer_arr[j] ="W"
        else:
            if answer_arr[j]=="G":
                continue
            elif answer_arr[j]=="W":
                answer_arr[j] ="G"
            else:
                answer_arr[j] ="B"


###############다음 부분을 고쳐야 한다. 
    B_count=0
    W_count=0
    G_count=0
    for a  in answer_arr:
        if a == "B":
            B_count+=1
        elif a == "W":
            W_count+=1
        elif a == "G":
            G_count+=1
        else:
            continue

    current = future
print(count)


