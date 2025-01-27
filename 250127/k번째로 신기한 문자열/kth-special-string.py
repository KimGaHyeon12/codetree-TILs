n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Write your code here!
answers = []
len_t = len(t)
for s in str:
    #print(s[:len_t])
    if s[:len_t] == t:
        answers.append(''.join(s))

answers.sort()
print(answers[k-1])
#print(answers )