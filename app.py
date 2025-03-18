import numpy as np


if __name__ == "__main__":
    with open("/inputs/size", "r") as f:
        size = int(f.read())

    array = np.random.random(size=size)
    total = np.sum(array)

    with open("/outputs/sum", "w") as f:
        f.write(str(total))
