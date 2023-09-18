# Time Complexity is O(n^2)
# Bubble sort sorts in an ascending order,
# loop run for n-1 times
# It first puts a larger value at the last.
def bubble_sort(n):
    for i in range(len(n) - 1):
        for j in range(len(n) - i - 1):
            if (n[j] > n[j + 1]):
                swapping(n, j)
    return n


def swapping(n, j):
    temp = n[j]
    n[j] = n[j + 1]
    n[j + 1] = temp


n = list(input())
print(bubble_sort(n))
