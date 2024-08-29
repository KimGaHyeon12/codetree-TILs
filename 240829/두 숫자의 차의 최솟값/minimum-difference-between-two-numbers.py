N = int(input())
str_arr = input()

arr = []
for i in range(N):
    arr.append(int(str_arr.split(" ")[i]))

#print(arr)

min_ = 200
for i in range(5):
    for j in range(5):
        cha = arr[i] - arr[j]
        if cha>0 and cha<min_:
            min_=cha

print(min_)