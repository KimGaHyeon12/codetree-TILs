a, b, c = map(int, input().split())

# Write your code here!

day, hour, mins = 11, 11, 11
elapsed_time = 0

while True:
    if day == a and hour == b and mins == c:
        break

    elapsed_time += 1
    mins += 1

    if mins == 60:
        hour += 1
        mins = 0
    if hour ==24:
        day += 1
        hour = 0

if a==11 and b==11 and c==11:
    print(0)
elif elapsed_time <= 0:
    print(-1)
else:
    print(elapsed_time)