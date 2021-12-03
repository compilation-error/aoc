import pandas as pd


def conv_to_bin(s: str):
    return int(s, 2)


def main():
    inputs = pd.read_csv("day3_input.csv", header=None)
    inputs[0] = inputs[0].map(str)
    inputs[0] = inputs[0].map(conv_to_bin)
    n = len(inputs)
    gamma = 0
    for i in range(12):
        mask = 2 ** i
        # print(f"{i=} {mask=:b} {inputs[0][0]:b}")
        # print(f"{(inputs[0][0] & mask):b}")
        # print((inputs[inputs[0] & mask == mask]))
        if len(inputs[inputs[0] & mask == mask]) >= n / 2:
            gamma += mask
    epsilon = 2 ** 12 - 1 - gamma
    print("part 1:", gamma, epsilon, gamma * epsilon)

    o2 = inputs.copy()
    co2 = inputs.copy()
    for i in reversed(range(12)):
        mask = 2 ** i
        if len(o2[o2[0] & mask == mask]) >= len(o2) / 2:
            o2 = o2[o2[0] & mask == mask]
        else:
            o2 = o2[o2[0] & mask != mask]
        if len(o2) == 1:
            o2value = o2[0].values[0]

        if len(co2[co2[0] & mask == mask]) >= len(co2) / 2:
            co2 = co2[co2[0] & mask != mask]
        else:
            co2 = co2[co2[0] & mask == mask]
        if len(co2) == 1:
            co2value = co2[0].values[0]

    print("part 2:", o2value * co2value)


if __name__ == "__main__":
    main()
