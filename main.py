class problemSolver:
    # Possible moves for different positions on numpad
    a = [[4, 6],
         [6, 8], [7, 9], [4, 8],
         [3, 9, 0], [], [1, 7, 0],
         [2, 6], [1, 3], [2, 4]]

    def __init__(self):
        pass

    def solve(self, position, n):
        if position == 5:
            return 1
        else:
            possiblePositions = [position]
            hop = 0
            print("Start position:", possiblePositions)
            while hop < n:
                hop += 1
                tempArray = []
                for i in possiblePositions:
                    tempArray += self.a[i]
                possiblePositions = tempArray
                print("Hop", hop, ":", possiblePositions)
            res = len(possiblePositions)
            return res


solver = problemSolver()
print(solver.solve(3, 3))

# Tests:
"""
position = 5, n = any -> 1
position = 1, n = 1   -> 2
position = 1, n = 2   -> 5
position = 1, n = 3   -> 10
position = 3, n = 3   -> 10
position = 0, n = 3   -> 12
"""
