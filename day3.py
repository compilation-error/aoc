import pandas as pd


def conv_to_bin(s: str):
    return int(s, 2)


def main():
    inputs = pd.read_csv("day3_input.csv", header=None)
    inputs[0] = inputs[0].map(str)
    inputs[0] = inputs[0].map(conv_to_bin)
    n = len(inputs)
    gamma = 0
    print(n)
    for i in range(12):
        mask = 2 ** i
        # print(f"{i=} {mask=:b} {inputs[0][0]:b}")
        # print(f"{(inputs[0][0] & mask):b}")
        # print((inputs[inputs[0] & mask == mask]))
        if len(inputs[inputs[0] & mask == mask]) >= n / 2:
            gamma += mask
    epsilon = 2 ** 12 - 1 - gamma
    print(gamma, epsilon, gamma * epsilon)


if __name__ == "__main__":
    main()
