from typing import List
import dataclasses


SIZE = 8


@dataclasses.dataclass
class Board:
    def __post_init__(self):
        self.grid = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

        self.grid[3][3] = 1
        self.grid[3][4] = 2
        self.grid[4][3] = 2
        self.grid[4][4] = 1

    def show(self):
        print("   a  b  c  d  e  f  g  h")

        for i, row in enumerate(self.grid):
            print(i + 1, row)

    # TODO: Only place in position without existing piece.
    def place(self, position: str, player: int):
        column = "abcdefgh".index(position[0])
        row = int(position[1]) - 1

        self.grid[row][column] = player


if __name__ == "__main__":
    board = Board()
    board.show()

    counter = 0

    while True:
        player = counter % 2 + 1
        position = input(f"\n{player} > ")

        board.place(position, player)
        board.show()

        counter += 1
