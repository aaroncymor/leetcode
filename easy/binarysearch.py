import math

def binarySearch(array, target):
    while array:
        first = 0
        last = len(array) - 1

        mid_index = int(math.floor((first + last) / 2))
        mid = array[mid_index]

        # element successfully searched
        if target == mid:
            return mid_index

        if target > mid:
            array = array[(mid_index + 1):]
        elif target < mid:
            array = array[:mid_index]
        
        real_index -= len(array)
        print(real_index)

    return -1

    

if __name__ == "__main__":
    binarySearch([1,2,3,4,5], 4)
    # print(binarySearch([1,2,3,4,5], 4))