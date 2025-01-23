a, b = map(int, input().split())

# Write your code here!
org = [a,b]
new = sorted(org)

big =  max(a,b)
small =  min(a,b)

small +=10
big = big *2

if  org == new:
    print(small,big)
else:
    print(big, small)