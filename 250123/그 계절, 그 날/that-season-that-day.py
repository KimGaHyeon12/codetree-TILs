Y, M, D = map(int, input().split())
  
m_days = [0,31,28,31,30,31,30,31,31,30,31,30,31,30,31,30]
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

answer = season(M)
if M!=2 and D > m_days[M]:
    answer = -1
elif M==2 and yun(Y)==True:
    if D <= 29:
        answer = season(M)
    else:     
        answer = -1
elif M==2 and yun(Y)==False:
    if D <= 28:
        answer = season(M)
    else:     
        answer = -1
else:
   answer = season(M)
    
print(answer)
#print(yun(Y))