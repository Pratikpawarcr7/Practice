from sklearn.datasets import load_iris

def main():

    print("-"*30)
    print("Iris Classification Case Study")
    print("-"*30)

    DataSet = load_iris()

    print("Indipendent Variable Are : ")
    print(DataSet.feature_name)

    print("Dependent Variables Are : ")
    print(DataSet.target_names)

if __name__ == "__main__":
    main()