def merge(nums1, m, nums2, n):
    # Вказівники з кінця
    i = m - 1          # реальна частина nums1
    j = n - 1          # nums2
    k = m + n - 1      # nums1

    # Поки є елементи в nums2
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    merge(nums1, 3, [2, 5, 6], 3)
    print(nums1)  # [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    merge(nums1, 1, [], 0)
    print(nums1)  # [1]

    nums1 = [0]
    merge(nums1, 0, [1], 1)
    print(nums1)  # [1]
