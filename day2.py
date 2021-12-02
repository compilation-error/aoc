import pandas as pd
import numpy as np


def main():
    commands = pd.read_csv("day2_input.csv", header=None, delimiter=" ")
    print(commands)
    x = sum(commands[commands[0] == "forward"][1])
    y = sum(commands[commands[0] == "down"][1]) - sum(commands[commands[0] == "up"][1])
    print(f"part 1: {x * y}")


if __name__ == "__main__":
    main()
