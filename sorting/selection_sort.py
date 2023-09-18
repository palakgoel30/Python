# Time complexity is O(n^2)
# selection sort sorts in an ascending order.
# Loop run n-1 times
# It puts smallest element at starting index.

def selection_sort(n):
    for i in range(len(n) - 1):
        smallest = i
        for j in range(i + 1, len(n)):
            if (n[smallest] > n[j]):
                smallest = j
        swapping(n, i, smallest)

    return n


def swapping(n, i, smallest):
    temp = n[smallest]
    n[smallest] = n[i]
    n[i] = temp


n = list(input())
print(selection_sort(n))
