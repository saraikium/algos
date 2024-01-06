def find_triplets(arr: list[int], k: int):
    arr.sort()  # Sort the array
    triplets = []
    n = len(arr)

    for i in range(n):
        if i > 0 and arr[i] == arr[i - 1]:  # Skip the same element to avoid duplicates
            continue
        left, right = i + 1, n - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == k:
                triplets.append((arr[i], arr[left], arr[right]))
                while left < right and arr[left] == arr[left + 1]:  # Skip duplicates
                    left += 1
                while left < right and arr[right] == arr[right - 1]:  # Skip duplicates
                    right -= 1
                left += 1
                right -= 1
            elif current_sum < k:
                left += 1
            else:
                right -= 1

    return triplets


# Example
arr = [-3, 2, 0, -5, 1, 5]
K = 0
triplets = find_triplets(arr, K)
print(triplets)
