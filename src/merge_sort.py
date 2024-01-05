def merge(left: list[int], right: list[int]) -> list[int]:
    len_left = len(left)
    len_right = len(right)

    if len_left == 0:
        return right

    if len_right == 0:
        return left

    merged: list[int] = []

    i = j = 0

    while i < len_left and j < len_right:
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len_left:
        merged.append(left[i])
        i += 1

    while j < len_right:
        merged.append(right[j])
        j += 1

    return merged


def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    start = 0
    end = len(arr)

    mid = start + end // 2
    left_sub_arr = merge_sort(arr[:mid])
    right_sub_arr = merge_sort(arr[mid:])

    return merge(left_sub_arr, right_sub_arr)


print(merge_sort([589, 27, 9273, 189, 174, 187, 224, 1, 24]))
