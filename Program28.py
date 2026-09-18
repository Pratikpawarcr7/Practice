from sklearn.datasets import load_breast_cancer
Border = "="*40

def main():

    DataSet = load_breast_cancer()

    print("Independent Variables Are : ")
    print(DataSet.feature_names)

    print("Dependent Variables Are : ")
    print(DataSet.target_names)
    

if __name__ == "__main__":
    main()