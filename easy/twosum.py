def twosum(nums, target):
    # brute force O(n)^2 time complexity
    for i in range(len(nums)):
        for j in range(i+1, len(nums), 1):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def twosum2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # using hashmap has O(n)
    h = {}
    for i, num in enumerate(nums):

        # if result of the difference of target and element
        # does not exist in dictionary 'h', add it as key
        # with the value as index.
        n = target - num
        if n not in h:
            # since we always begin with an empty dictionary,
            # we continue looping until we retrieve (or finish loop)
            # the result of (target - num). The retrieved value is always
            # the first index, the second one is the index of the num/element
            """
            e.g, passed nums is list [2, 7, 11, 15] then h should be:
                {
                    2: 0,
                    7: 1,
                    11: 2,
                    15: 3
                }
            """
            h[num] = i
        else:
            return [h[n], i]

def twoSum3(nums, target):
    # assuming array is sorted, else sort the array here
    # sorting algorithm here

    # comparison algorithm here
    left = 0
    right = len(nums) - 1

    while (left < right) and (right > left):
        currSum = nums[left] + nums[right]
        if currSum == target:
            return [nums[left], nums[right]]
        elif currSum > target: # move right 1 place to the left
            right -= 1
        elif currSum < target: # move left 1 place to the right
            left += 1
    return []


if __name__ == '__main__':
    print(twoSum3([2,7,11,15], 14))
