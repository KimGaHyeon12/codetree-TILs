binary_string = input()

# Write your code here!
binary = [int(b) for b in binary_string]
num = 0

for i in range(5):
    num = num * 2 + binary[i]

print(num)
