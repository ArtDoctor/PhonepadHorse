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
            possiblePositions = [0]*10
            possiblePositions[position] = 1
            hop = 0
            print("Start positions:", possiblePositions)
            while hop < n:
                # Every hop we calculate for each possible position possible positions
                hop += 1
                tempArray = [0]*10
                for i in range(0, len(possiblePositions)):
                    moves = self.numPadMoves[i]
                    for move in moves:
                        tempArray[move] += possiblePositions[i]
                possiblePositions = tempArray
                print("Hop", hop, ":", possiblePositions)
            # Result is the amount of possible positions
            res = sum(possiblePositions)
            # They will be distinct for sure
            return res


solver = problemSolver()
print(solver.solve(0, 3))

# Tests:
"""
position = 5, n = any -> 1
position = 1, n = 1   -> 2
position = 1, n = 2   -> 5
position = 1, n = 3   -> 10
position = 3, n = 3   -> 10
position = 0, n = 3   -> 12
"""
