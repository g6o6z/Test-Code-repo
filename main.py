import matplotlib.pyplotas as plt
import numpy as np

def main():
    a=1
    b=2
    print(calc(a,b))

def calc(a,b):
    return np.dot((a+b),a)*b


if __name__ == "__main__":
    main()