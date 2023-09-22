def conquer(left, right):
    merged = []
    left_index, right_index = 0, 0
    while ((left_index < len(left)) and (right_index < len(right))):
        if (left[left_index] < right[right_index]):
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append((right[right_index]))
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

def divide(n):
    if len(n) <=1:   # to avoid recursion goes on in loop
        return n
    mid = len(n) // 2  # to find the mid-value
    left_ele = n[:mid]
    right_ele = n[mid:]
    left = divide(left_ele)  # to divide every element in a single sorted element
    right = divide(right_ele)
    return conquer(left, right)  # this function call to merge the sorted element while comparing


n = [6, 3, 9, 5, 2, 8]
print((divide(n)))
