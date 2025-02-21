m1, d1, m2, d2 = map(int, input().split())
A = input()

# Write your code here!




def num_of_days(m, d):
    # 계산 편의를 위해 월마다 몇 일이 있는지를 적어줍니다. 
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0
    
    # 1월부터 (m - 1)월 까지는 전부 꽉 채워져 있습니다.
    for i in range(1, m):
        total_days += days[i]
    
    # m월의 경우에는 정확이 d일만 있습니다.
    total_days += d
    
    return total_days    


# 두 날짜간의 차이가 몇 일인지를 구합니다.
diff = num_of_days(m2, d2) - num_of_days(m1, d1)
# 음수인 경우에는, 양수로 넘겨 계산해주면 올바르게 계산이 됩니다. 
while diff < 0:
    diff += 7


answer = diff//7

# 알맞은 요일의 이름을 출력합니다.
day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#print(day_of_week[diff % 7])
#print(day_of_week .index("Sat"))
if (diff%7) <= (day_of_week.index(A)):
    answer +=1
print(answer)

