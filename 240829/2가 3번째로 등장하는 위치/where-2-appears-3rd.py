N = int(input())
input_str = input() 

input_arr=[]
for i in range(N):
    input_arr.append(int(input_str.split(' ')[i]))

 
count=0
c=0
for i in input_arr:
    c=c+1
    if i==2:
        count = count +1
        if count ==3:
            print(c)
            break