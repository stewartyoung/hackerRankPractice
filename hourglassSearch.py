inputArray = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0,0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

def hourglassSum(arr):
    numRows = len(arr)
    numCols = len(arr[0])
    # # create an array for (x -2)(y-2) to store hourglass 
    # hourglassArray = [[0 for x in range(numCols - 2)] for y in range(numRows - 2)]
    
    # iniate storage variable for max hourglass we encounter
    maxHourglass = -200000
    # loop through first to second last row of the matrix 
    for i in range(numRows -2):
        # loop through second to second last element of each row
        for j in range(1, numCols - 1):
            topH = arr[i][j - 1] + arr[i][j] + arr[i][j + 1]
            middleH = arr[i+1][j]
            bottomH = arr[i+2][j-1] + arr[i+2][j] + arr[i+2][j+1]
            totalH = topH + middleH + bottomH
            
            if totalH > maxHourglass:
                maxHourglass = totalH
    
    return maxHourglass
    

print(hourglassSum(inputArray))