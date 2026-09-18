from sklearn.datasets import load_breast_cancer
Border = "="*40

def main():

    DataSet = load_breast_cancer()

    for i in range(len(DataSet.target)):
        print("ID %d Features %s Labels %s "%(i,DataSet.data[i],DataSet.target[i]))
    

if __name__ == "__main__":
    main()