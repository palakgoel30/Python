# Time complexity is O(n^2)
# Divided into unsorted and sorted part.
def insertion_sort(n):
    for i in range(1,len(n)):
        current_ele = n[i]
        j = i-1
        while(j>=0 and current_ele < n[j]):
            n[j+1] = n[j]
            j -= 1
        n[j+1] = current_ele
    return n

n = list(input())
print(insertion_sort(n))




