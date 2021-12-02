import pandas as pd


def main():
    commands = pd.read_csv("day2_input.csv", header=None, delimiter=" ")
    """
    forward X increases the horizontal position by X units.
    down X increases the depth by X units.
    up X decreases the depth by X units.
    """
    x = sum(commands[commands[0] == "forward"][1])
    y = sum(commands[commands[0] == "down"][1]) - sum(commands[commands[0] == "up"][1])
    print(f"part 1: {x * y}")

    """
    down X increases your aim by X units.
    up X decreases your aim by X units.
    forward X does two things:
        It increases your horizontal position by X units.
        It increases your depth by your aim multiplied by X.
    """
    x = 0
    y = 0
    z = 0
    for i, row in commands.iterrows():
        if row[0] == "forward":
            x += row[1]
            y += row[1] * z
        elif row[0] == "down":
            z += row[1]
        elif row[0] == "up":
            z -= row[1]
    print(f"part 2: {x * y}")


if __name__ == "__main__":
    main()
