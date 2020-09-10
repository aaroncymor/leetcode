def insertionSort(array):
    for i in range(1, len(array)):
        tmpIdx = i
        for j in range(i-1, -1, -1):
            if array[tmpIdx] < array[j]:
                swap(array, tmpIdx, j)
                tmpIdx = j
    return array


def swap(array, idxOne, idxTwo):
    tmp = array[idxOne]
    array[idxOne] = array[idxTwo]
    array[idxTwo] = tmp



if __name__ == "__main__":
    print(insertionSort([8,5,2,9,5,6,7]))