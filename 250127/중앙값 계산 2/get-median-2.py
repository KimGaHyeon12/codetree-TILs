n = int(input())
arr = list(map(int, input().split()))

# Write your code here!

answers = []
for i in range(1,n+1):
    if i%2 != 0:
        new_arr = arr[:i]
        new_arr.sort()
        #print(i, new_arr)
        answers.append(new_arr[i//2])

for a in answers:
    print(a,'',end='' )
#print(answers )

