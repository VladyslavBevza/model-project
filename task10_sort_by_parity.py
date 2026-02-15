def sortArrayByParity(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] % 2 > nums[right] % 2:
            nums[left], nums[right] = nums[right], nums[left]

        if nums[left] % 2 == 0:
            left += 1

        if nums[right] % 2 == 1:
            right -= 1

    return nums


if __name__ == "__main__":
    print(sortArrayByParity([3, 1, 2, 4]))  # [2, 4, 3, 1] (варіанти допустимі)
    print(sortArrayByParity([0]))           # [0]
