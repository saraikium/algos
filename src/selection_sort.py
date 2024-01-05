def selection_sort(input: list[int]) -> list[int]:
    n = len(input)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if input[j] < input[i]:
                min_index = j

        (input[i], input[min_index]) = (input[min_index], input[i])

    return input


arr = [589, 27, 9273, 189, 174, 187, 224, 1]
print(selection_sort(arr))
