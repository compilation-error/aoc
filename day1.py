import pandas as pd
import numpy as np


def main():
    depths = pd.read_csv("day1_input.csv", header=None)
    dsign = np.sign(depths.tail(-1)[0].values - depths.head(-1)[0].values)
    dsum = np.sum(dsign[dsign > 0])
    print(dsum)


if __name__ == "__main__":
    main()
