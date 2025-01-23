Y, M, D = map(int, input().split())
answer = -1 
m_days = [0,31,30,31,30,31,30,31,31,30,31,30,31,30,31,30]
# Write your code here!
#어떤 계절인지.
def season(M):
    if 3<=M<=5:
        return "Spring"
    elif 6<=M<=8:
        return "Summer"
    elif 9<=M<=11:
        return "Fall"
    else:
        return "Winter"

def yun(Y):
    if Y%400 ==0:
        return True
    elif Y%100 ==0:
        return False
    elif Y%4==0:
        return True
    else:
        return False

if D > m_days[M]:
    answer = -1
elif M==2 and yun(Y)==True and D > 29:
    answer = -1
else:
   answer = season(M)
    
print(answer)