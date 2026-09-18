from sklearn.datasets import load_breast_cancer
Border = "="*40

def main():

    DataSet = load_breast_cancer()

    print(Border)
    print("Independent Variables Are : ")
    print(DataSet.feature_names)
    print(Border)

  
    print(Border)
    print("Length Of Independent Variables Are : ")
    print(len(DataSet.feature_names))
    print(Border)  

 
    print(Border)
    print("Dependent Variables Are : ")
    print(DataSet.target_names)
    print(Border) 

    print(Border)
    print("Length of Dependent Variables Are : ")
    print(len(DataSet.target_names))
    print(Border)    

if __name__ == "__main__":
    main()