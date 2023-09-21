# Time complexity is O(n^2)
# Split a list into 2 parts unsorted and sorted array.
def insertion_sort(n):
    for i in range(1,len(n)):
        current_ele = n[i]
        j = i-1
        while(j>=0 and current_ele < n[j]): # Compare the current element to next element
            n[j+1] = n[j]
            j -= 1
        n[j+1] = current_ele
    return n

n = list(input())
print(insertion_sort(n))




