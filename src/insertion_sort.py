def insertion_sort(input: list[int]) -> list[int]:
    for i in range(1, len(input)):
        key = input[i]
        j = i - 1
        # Move elements from i - 1 to 0 one position to the right,
        # until we find the right place for the key to insert
        # at which point we insert the key in that place.
        # thus the sub array A[0: i -1] always remains sorted
        while j >= 0 and input[j] > key:
            input[j + 1] = input[j]
            j = j - 1
        else:
            input[j + 1] = key

    return input


arr = [589, 27, 9273, 189, 174, 187, 224, 1]
print(insertion_sort(arr))
