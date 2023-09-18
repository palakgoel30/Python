n = [7,8,3,1,2]
for i in range(len(n)-1):
    for j in range(len(n)-i-1):
        if(n[j] > n[j+1]):
            temp = n[j]
            n[j] = n[j+1]
            n[j+1] = temp
print(n)
