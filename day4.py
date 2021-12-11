import numpy as np


class Bingo:

    def __init__(self, board):
        self.board = np.array(board)
        self._board = np.array([[0 for i in range(len(board))] for j in range(len(board))])
        self.size = len(board)

    def check_off(self, number: int) -> None:
        self._board[np.where(self.board == number)] = 1

    def verify_board(self) -> bool:
        return (self.size in (*np.sum(self._board, axis=0), *np.sum(self._board, axis=1)))


def main():
    with open("day4_input.txt", 'r') as file:
        lines = file.readlines()

    numbers = [int(n) for n in lines[0].split(",")]

    boards = []
    b = []
    for line in lines[1:]:
        if len(line.strip()) == 0:
            continue
        b.append([int(x) for x in line.strip().split()])
        if len(b) == 5:
            boards.append(Bingo(b))
            b = []

    return_number_1, return_number_2 = 0, 0
    for n in numbers:
        if len(boards) == 1:
            b = boards[0]
            b.check_off(n)
            if b.verify_board():
                if return_number_2 == 0:
                    return_number_2 = n * np.sum(b.board[np.where(b._board == 0)])
                boards.remove(b)
                break
        else:
            for i, b in enumerate(boards):
                b.check_off(n)
                if (b.verify_board()):
                    if return_number_1 == 0:
                        return_number_1 = n * np.sum(b.board[np.where(b._board == 0)])
                    boards.remove(b)

    print(f"part 1: {return_number_1}")
    print(f"part 2: {return_number_2}")


if __name__ == "__main__":
    main()
