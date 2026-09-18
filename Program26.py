from sklearn.datasets import load_breast_cancer
Border = "="*40

def main():

    DataSet = load_breast_cancer()

    print(DataSet)
    

if __name__ == "__main__":
    main()