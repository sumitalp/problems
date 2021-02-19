def sumOfFirsts(numbers):
    res = 0

    def findIndex(nums):
        for i, v in enumerate(nums):
            if v != 0:
                return i, v

        return -1, -1

    while len(numbers) != numbers.count(0):
        index, value = findIndex(numbers)

        if value != -1:
            for i in range(index, len(numbers)):
                if numbers[i] >= value:
                    numbers[i] -= value
                else:
                    break

            res += value

    return res

print(sumOfFirsts([3,3,5,2,3]))
assert sumOfFirsts([3,3,5,2,3]) == 6

print(sumOfFirsts([5,5,5,5,5]))
assert sumOfFirsts([5,5,5,5,5]) == 5