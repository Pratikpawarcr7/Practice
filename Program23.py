import pandas as pd

Border = "-"*30

def Load_cSv():

    DataPath = "iris.csv"

    print(Border)
    print(" Step 1 : Load The Data ")
    print(Border)

    df = pd.read_csv(DataPath)

    print("DataLoad Successfully")
    print("Intially Entries OF Data")
    print(df.head)

def main():
    Load_cSv()

if __name__ == "__main__":
    main()