arr= []
for _ in range(5):
    arr.append(list(map(str,input().split())))

 
 
new_arr= []
for item  in arr:
    temp = []
    for i in item:
        u = i.upper()
        temp.append(u)
    new_arr.append(temp)

print(new_arr)