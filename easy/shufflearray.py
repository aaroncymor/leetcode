def shuffle(nums, n):
    res = []
    start = 0

    if len(nums) != (2 * n):
        raise ValueError("Error")

    # this generates indices
    # starting from n, and ends with
    # (n * 2). Index starts at 0, so
    # range(4, 8) = [4, 5, 6, 7]
    for i in range(n, n*2):
        res.append(nums[i - n])
        res.append(nums[i])
    return res

if __name__ == '__main__':
    print(shuffle([1,2,3,4,4,3,2,1], 4))