import pandas as pd

def main():

    sobj = pd.Series( [11,12,13,14],index = [9,8,7,6])

    print(sobj)

    print(type(sobj))
if __name__ == "__main__":
    main()