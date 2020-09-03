def productSum(array):
    depth1Sum = 0
    for depth1El in array:
        if type(depth1El) == int:
            # depth1El is an integer
            depth1Sum += depth1El
        elif type(depth1El) == list:
            depth2Sum = 0
            # depth1El is a list
            for depth2El in depth1El:
                if type(depth2El) == int:
                    # depth2El is an integer
                    depth2Sum += depth2El
                elif type(depth2El) == list:
                    depth3Sum = 0
                    # depth3El is a list and final depth
                    for depth3El in depth2El:
                        depth3Sum += depth3El
                    depth3Sum *= 3
                    depth2Sum += depth3Sum
            depth2Sum *= 2
            depth1Sum += depth2Sum
    return depth1Sum

def productSum(array):
    return productSumHelper(array)


def productSumHelper(array, multiplyBy=1):
    currSum = 0
    for item in array:
        if type(item) == int:
            currSum += item
        elif type(item) == list:
            currSum += productSumHelper(item, multiplyBy + 1)
    currSum = currSum * multiplyBy
    return currSum




if __name__ == "__main__":
    # print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
    # print(iterateRecursively(4))
    print(productSumHelper([5,2,[7,-1],3,[6,[-13, 8],4]]))