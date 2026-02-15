def sortedSquares(nums):
    n = len(nums)
    result = [0] * n

    left = 0
    right = n - 1
    position = n - 1

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[position] = nums[left] ** 2
            left += 1
        else:
            result[position] = nums[right] ** 2
            right -= 1
        position -= 1

    return result


if __name__ == "__main__":
    print(sortedSquares([-4, -1, 0, 3, 10]))  # [0, 1, 9, 16, 100]
    print(sortedSquares([-7, -3, 2, 3, 11]))  # [4, 9, 9, 49, 121]
