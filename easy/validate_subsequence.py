def isValidSubsequence(array, sequence):
    sequenceCheck = -1

    for item in sequence:
        if item not in array:
            return False
        
        for idx, num in enumerate(array):
            if item == num:
                if sequenceCheck < idx:
                    sequenceCheck = idx
                    array[idx] = None
                    break
                else:
                    return False
    return True


if __name__ == "__main__":
    print(isValidSubsequence([1, 1, 1, 1, 1, 1], [1, 1, 1]))
