def replaceElements(arr):
    max_right = -1

    # Проходимо справа наліво
    for i in range(len(arr) - 1, -1, -1):
        current = arr[i]
        arr[i] = max_right
        max_right = max(max_right, current)

    return arr


if __name__ == "__main__":
    print(replaceElements([17, 18, 5, 4, 6, 1]))  # [18, 6, 6, 6, 1, -1]
    print(replaceElements([400]))                # [-1]
