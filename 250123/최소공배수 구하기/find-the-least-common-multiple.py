n, m = map(int, input().split())

# Write your code here!

answer = -1
n_arr = []
m_arr = []
for i in range(1,max(n,m)):
    n_arr.append(n*i)
    m_arr.append(m*i)

for n_ in n_arr:
    if n_ in m_arr:
        print(n_)
        break