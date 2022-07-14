class problemSolver:
    # Possible moves for different positions on numpad
    numPadMoves = [[4, 6],
                   [6, 8], [7, 9], [4, 8],
                   [3, 9, 0], [], [1, 7, 0],
                   [2, 6], [1, 3], [2, 4]]

    def solve(self, position, n):
        # In position 5 there are no possible moves
        if position == 5:
            return 1
        else:
            possiblePositions = [position]
            hop = 0
            print("Start position:", possiblePositions)
            while hop < n:
                # Every hop we calculate for each possible position possible positions
                hop += 1
                tempArray = []
                for i in possiblePositions:
                    tempArray += self.numPadMoves[i]
                possiblePositions = tempArray
                print("Hop", hop, ":", possiblePositions)
            # Result is the amount of possible positions
            res = len(possiblePositions)
            # They will be distinct for sure
            return res


solver = problemSolver()
print(solver.solve(1, 3))

# Tests:
"""
position = 5, n = any -> 1
position = 1, n = 1   -> 2
position = 1, n = 2   -> 5
position = 1, n = 3   -> 10
position = 3, n = 3   -> 10
position = 0, n = 3   -> 12
"""
