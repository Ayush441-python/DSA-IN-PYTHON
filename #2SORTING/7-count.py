def count_sort(arr):
    if not arr:
        return arr

    mx = max(arr)
    count = [0] * (mx + 1)

    for num in arr:
        count[num] += 1

    idx = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[idx] = i
            idx += 1
            count[i] -= 1

    return arr
