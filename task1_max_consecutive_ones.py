def findMaxConsecutiveOnes(nums):
    max_count = 0
    current_count = 0

    for num in nums:
        if num == 1:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0

    return max_count


if __name__ == "__main__":
    # Тестування
    print(findMaxConsecutiveOnes([1,1,0,1,1,1]))  # 3
    print(findMaxConsecutiveOnes([1,0,1,1,0,1]))  # 2
