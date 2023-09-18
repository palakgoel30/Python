n = [7,8,3,1,2]

for i in range(len(n)-1):
    smallest = i
    for j in range(i+1,len(n)):
        if(n[smallest] > n[j]):
            smallest = j
    temp = n[smallest]
    n[smallest] = n[i]
    n[i] = temp
print(n)

