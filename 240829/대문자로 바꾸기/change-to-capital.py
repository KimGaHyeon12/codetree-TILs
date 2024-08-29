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

for item  in new_arr:
 
    for i in item:
        print(i,' ',end = '')
    print()