def duplicateZeros(arr):
    n = len(arr)
    result = []

    for num in arr:
        result.append(num)
        if num == 0:
            result.append(0)

    # обрізаємо до початкової довжини
    for i in range(n):
        arr[i] = result[i]

    return arr


if __name__ == "__main__":
    print(duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]))  # [1, 0, 0, 2, 3, 0, 0, 4]
    print(duplicateZeros([1, 2, 3]))                # [1, 2, 3]
