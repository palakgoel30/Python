def bubble_sort(n):
    for i in range(len(n) - 1):
        for j in range(len(n) - i - 1):
            if (n[j] > n[j + 1]):
                temp = n[j]
                n[j] = n[j + 1]
                n[j + 1] = temp
    return n


n = list(input())
print(bubble_sort(n))
