import pandas as pd

def main():

    Data = ([11,12,13,14])

    sobj = pd.Series(Data)

    print(sobj)

    print(type(sobj))
if __name__ == "__main__":
    main()