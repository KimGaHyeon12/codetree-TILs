arr= []
for _ in range(5):
    arr.append(list(map(str,input().split())))

 
s2 = [item.upper() for item in arr]  # Convert each string in the list to uppercase
print(s2)