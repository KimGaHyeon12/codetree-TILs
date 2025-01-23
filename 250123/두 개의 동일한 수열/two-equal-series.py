n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Write your code here!
answer = "Yes"
for s_a in A:
    if s_a not in B:
        answer = "No"

for s_b in B:
    if s_b not in A:
        answer = "No"

print(answer)