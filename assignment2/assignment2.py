from typing import List


def get_average_elevation(m: List[List[int]]) -> float:
    """
    Returns the average elevation across the elevation map m.

    Examples
    >>> get_average_elevation([])
    0
    >>> m = [[1,2,3],[4,5,6],[7,8,9]]
    >>> get_average_elevation(m)
    5.0
    >>> m = [[1,2,2,5],[4,5,4,8],[7,9,9,1],[1,2,1,4]]
    >>> get_average_elevation(m)
    4.0625
    """
    #Your code goes here

    if m is None or len(m) == 0:
        return 0

    average = 0.0

    for i in m:
        for j in i:
            average += j

    average /= len(m) ** 2

    return average


def find_peak(m: List[List[int]]) -> List[int]:
    """
    Given an non-empty elevation map m, returns the cell of the
    highest point in m.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,2,3],
             [9,8,7],
             [5,4,6]]
    >>> find_peak(m)
    [1,0]
    >>> m = [[6,2,3],
             [1,8,7],
             [5,4,9]]
    >>> find_peak(m)
    [2,2]
    """
    #Your code goes here

    ans = []
    largest = 0

    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] > largest:
                largest = m[i][j]
                ans = [i,j]
    return ans


def is_sink(m: List[List[int]], c: List[int]) -> bool:
    """
    Returns True if and only if c is a sink in m.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,2,3],
             [2,3,3],
             [5,4,3]]
    >>> is_sink(m, [0,0])
    True
    >>> is_sink(m, [2,2])
    True
    >>> is_sink(m, [3,0])
    False
    >>> m = [[1,2,3],
             [2,1,3],
             [5,4,3]]
    >>> is_sink(m, [1,1])
    True
    """
    #Your code goes here
    i = c[0]
    j = c[1]

    if i < 0 or i >= len(m) or j < 0 or j >= len(m):
        return False

    adj=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

    for x in adj:

        adjcellx = i + x[0]
        adjcelly = j + x[1]

        if 0 <= adjcellx < len(m) and 0 <= adjcelly < len(m):
            if m[adjcellx][adjcelly] < m[i][j]:
                return False

    return True


def find_local_sink(m: List[List[int]], start: List[int]) -> List[int]:
    """
    Given a non-empty elevation map, m, starting at start,
    will return a local sink in m by following the path of lowest
    adjacent elevation.
    # start will always exist in m
    Examples (note some spacing has been added for human readablity)
    >>> m = [[ 5,70,71,80],
             [50, 4,30,90],
             [60, 3,35,95],
             [10,72, 2, 1]]
    >>> find_local_sink(m, [0,0])
    [3,3]
    >>> m = [[ 5,70,71,80],
             [50, 4, 5,90],
             [60, 3,35, 2],
             [ 1,72, 6, 3]]
    >>> find_local_sink(m, [0,3])
    [2,3]
    >>> m = [[9,2,3],
             [6,1,7],
             [5,4,8]]
    >>> find_local_sink(m, [1,1])
    [1,1]
    """
    #Your code goes here
    def helper(m, c):

        mapLength = len(m)
        lowestCell = [c[0], c[1]]

        for i in range(-1, 2):
            for j in range(-1, 2):

                # ignore cell itself
                if i == 0 and j == 0:
                    continue
                # skips rows out of index
                if i + c[0] < 0 or i + c[0] >= mapLength:
                    continue
                # skips cols out of index
                if j + c[1] < 0 or j + c[1] >= mapLength:
                    continue

                # update lowestCell once we find a smaller one
                if m[i + c[0]][j + c[1]] < m[lowestCell[0]][lowestCell[1]]:
                    lowestCell = [i + c[0], j + c[1]]

        return lowestCell

    i = start[0]
    j = start[1]
    lowestIndex = [i, j]

    while True:
        lowestAmongNeighbours = helper(m,lowestIndex)
        if lowestAmongNeighbours == lowestIndex:
            return lowestIndex
        lowestIndex = lowestAmongNeighbours


def can_hike_to(m: List[List[int]], s: List[int], d: List[int], supplies: int) -> bool:
    """
    Given an elevation map m, a start cell s, a destination cell d, and
    the an amount of supplies returns True if and only if a hiker could reach
    d from s using the strategy dscribed in the assignment .pdf. Read the .pdf
    carefully. Assume d is always south, east, or south-east of s. The hiker
    never travels, north, west, nor backtracks.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,4,3],
             [2,3,5],
             [5,4,3]]
    >>> can_hike_to(m, [0,0], [2,2], 4)
    True
    >>> can_hike_to(m, [0,0], [0,0], 0)
    True
    >>> can_hike_to(m, [0,0], [2,2], 3)
    False
    >>> m = [[1,  1,100],
             [1,100,100],
             [1,  1,  1]]
    >>> can_hike_to(m, [0,0], [2,2], 4)
    False
    >>> can_hike_to(m, [0,0], [2,2], 202)
    True
    """
    #Your code goes here
    if s == d:
        return True

    i = s[0]
    j = s[1]

    while [i,j] != d:

        # choose East
        if i == d[0] or (j+1<len(m) and
                         abs(m[i][j + 1] - m[i][j]) <= abs(m[i + 1][j] - m[i][j])):
            supplies -= abs(m[i][j + 1] - m[i][j])
            j += 1

        # choose South
        else:
            supplies -= abs(m[i + 1][j] - m[i][j])
            i += 1

        # Running out of supplies
        if supplies < 0:
            return False

    return True


def rotate_map(m: List[List[int]]) -> None:
    """
    Rotates the orientation of an elevation map m 90 degrees counter-clockwise.
    See the examples to understand what's meant by rotate.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,2,3],
             [2,3,3],
             [5,4,3]]
    >>> rotate_map(m)
    >>> m
    [[3,3,3],
     [2,3,4],
     [1,2,5]]
    >>> m = [[5,9,1,8],
             [2,4,5,7],
             [6,3,3,2],
             [1,7,6,3]]
    >>> rotate_map(m)
    >>> m
    [[8,7,2,3],
     [1,5,3,6],
     [9,4,3,7],
     [5,2,6,1]]
    """
    #Your code goes here

    # First Transpose the matrix
    mapLength = len(m)
    for i in range(mapLength):
        for j in range(i, mapLength):
            # swap them
            m[i][j], m[j][i] = m[j][i], m[i][j]

    # Then Reverse Every col
    for i in range(mapLength):
        j = 0
        k = mapLength - 1
        while j < k:
            m[j][i], m[k][i] = m[k][i], m[j][i]
            j += 1
            k -= 1



"""
You are not required to understand or use the code below. It is there for
curiosity and testing purposes.
"""
def create_real_map()-> List[List[int]]:
    """
    Creates and returns an elevation map from the real world data found
    in the file elevation_data.csv.

    Make sure this .py file and elevation_data.csv are in the same directory
    when you run this function to ensure it works properly.
    """
    data = open("elevation_data.csv")
    m = []
    for line in data:
        m.append(line.split(","))
    data.close()
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = int(m[i][j])
    return m













