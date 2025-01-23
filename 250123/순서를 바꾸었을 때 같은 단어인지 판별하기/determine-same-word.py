word1 = input()
word2 = input()

# Write your code here!
count_dic = { }
 
answer = "Yes" 

if len(word1) != len(word2):
    answer = "No" 
else:
    for w1 in word1:
        if w1 in count_dic.keys():
            count_dic[w1] += 1
        else:
            count_dic[w1] = 1

    for w2 in word2:
        if w2 in count_dic.keys() and count_dic[w2] > 0:
            count_dic[w2] -= 1
        else:
            answer = "No" 
            break


print(answer)