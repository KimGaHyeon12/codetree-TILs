n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
count_B = 0
count_W = 0
answer = ["" for _ in range(100)]
current = 0

for t in range(n):
    if dir[t] =="R":
        if current + x[t] <100:
            for i in range(current,current + x[t]): 
                answer[i] ="B"
            current = current + x[t]
        else:
            for i in range(current,current + x[t]): 
                answer[i] ="B"
                if current+i>1:
                    break
            for i in range(current + x[t] -100):
                 answer[i] ="B"
            current = current + x[t]

    else: #"L"
        if current - x[t] >0:
            for i in range(current - x[t], current): 
                answer[i] ="W"
            current = current - x[t]

        else: 
            for i in range( current): 
                answer[i] ="W"
            for i in range( current - x[t],0): 
                answer[i] ="W"
                if current-i < 0:
                    break
            current = current - x[t]


#print(answer)
for a in answer:
    if a =="B":
        count_B +=1
    elif a =="W":
        count_W +=1
 
print(count_W, count_B)


