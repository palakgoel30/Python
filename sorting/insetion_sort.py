n = [7,8,3,1,2]
for i in range(1,len(n)):
    current_ele = n[i]
    j = i-1
    while(j>=0 and current_ele < n[j]):
        n[j+1] = n[j]
        j = j -1
    n[j+1] = current_ele
print(n)





