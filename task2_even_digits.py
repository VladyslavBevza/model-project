def findNumbers(nums):
    count = 0

    for num in nums:
        #рахуємо кількість цифр
        if len(str(num)) % 2 == 0:
            count += 1

    return count


if __name__ == "__main__":
    print(findNumbers([12, 345, 2, 6, 7896]))   # 2
    print(findNumbers([555, 901, 482, 1771]))   # 1
