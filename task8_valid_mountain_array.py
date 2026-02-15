def validMountainArray(arr):
    n = len(arr)

    if n < 3:
        return False

    i = 0

    # Підйом вгору
    while i + 1 < n and arr[i] < arr[i + 1]:
        i += 1

    # Пік не може бути першим або останнім
    if i == 0 or i == n - 1:
        return False

    # Спуск вниз
    while i + 1 < n and arr[i] > arr[i + 1]:
        i += 1

    return i == n - 1


if __name__ == "__main__":
    print(validMountainArray([2, 1]))        # False
    print(validMountainArray([3, 5, 5]))     # False
    print(validMountainArray([0, 3, 2, 1]))  # True
