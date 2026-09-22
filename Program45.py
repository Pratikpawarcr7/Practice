import pandas as pd

def main():

    sobj = pd.Series([11.5,12,True,"Sager"])

    print(sobj)

    print(type(sobj))
if __name__ == "__main__":
    main()