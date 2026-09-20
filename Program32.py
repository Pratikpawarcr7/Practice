# Step 1 : Load the DataSet
# Step 2 : Analyze the Data
# step 3 : Decide indipendent and dependent
# step 4 : Visulize the Data
# step 5 : Train split (from sklearn.model_selection import train_test_split)
# step 6 : Decide the Modul (from sklearn.tree import DecisionTreeClassifier)
# step 7 : Train the Module
# step 9 : Test the Module
# step 9 : Evaluate the mdoel performance

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

Border = "="*60
#==============================================================================================
# Step 1 : Load the DataSet
#==============================================================================================

print(Border)
print("Step 1 : Load the DataSet")
print(Border)


DataPath = "iris.csv"

df = pd.read_csv(DataPath)

print("DataSet Loaded Successfully")
print("Initial Values Of DataSet : ")
print(df.head)

#==============================================================================================
# Step 2 : Analyze the Data (EDA)
#==============================================================================================


print(Border)
print("Step 2 : Analyze the Data (EDA)")
print(Border)

print("Columns of Dataset : ")
print(list(df.columns))

print("Shape  of Dataset : ")
print(df.shape)

print("Missing Values of DataSet : ")
print(df.isnull().sum())

print("Distribution of DataSet(Species) : ")
print(df["species"])

print("tatistical Report ")
print(df.describe())

#==============================================================================================
# step 3 : Decide The Indipendent and Dependent Variables
#==============================================================================================

print(Border)
print("step 3 : Decide The Indipendent and Dependent Variables")
print(Border)

featur_col = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
    ]

X = df[featur_col]
Y = df["species"]

print("Shap of X : ",X.shape)
print("Shap of Y : ",Y.shape)

#==============================================================================================
# step 4 : Visulize the Data
#==============================================================================================

print(Border)
print("step 4 : Visulize the Data")
print(Border)

plt.figure(figsize=(7,5))

for sp in df["species"].unique():
    temp = df[df["species"]==sp]
    plt.scatter(temp["petal length (cm)"],temp["petal width (cm)"],label = sp)

plt.title("Marvellous Iris Case Study ")

plt.xlabel("petal length (cm)")
plt.ylabel("petal weigth (cm)")

plt.legend()
plt.grid()
plt.show()

#==============================================================================================
# step 5 : Train_Test_Split the DataSet
#==============================================================================================

print(Border)
print("step 5 : Train_Test_Split the DataSet")
print(Border)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

print("DataSplit Successfully : ")

print("Shape of X :",X.shape)
print("Shape of Y :",Y.shape)

print("Shape of X_train",X_train.shape)
print("Shape of X_test",X_test.shape)

print("Shape of Y_train",Y_train.shape)
print("Shape of Y_test",Y_test.shape)

#==============================================================================================
# step 6 : Decide the Module
#==============================================================================================

print(Border)
print("Step 6 : Decide the Module")
print(Border)

model = DecisionTreeClassifier(max_depth=5)

print("Module Gets Created Successfully : ")


#==============================================================================================
# Step 7 : Train The Module
#==============================================================================================

print(Border)
print("Step 7 : Train The Module")
print(Border)

model.fit(X_train,Y_train)

print("Module Train Successfully")

#==============================================================================================
# Step 8 : Test The Module
#==============================================================================================

print(Border)
print("Step 8 : Test The Module")
print(Border)

Y_Pred = model.predict(X_test)

print("Model testing done")

print("Expected Answer : ")
print(Y_test)

print("Predicted Answer : ")
print(Y_Pred)

#==================================================================================================================================
# Step 9 : Evaluate the mdoel performance
#==================================================================================================================================

print(Border)
print("Step 9 : Evaluate the mdoel performance")
print(Border)

accurancy = accuracy_score(Y_test,Y_Pred)
print("Accurancy of Module is : ",accurancy*100)

print("Confusion Matrix : ")
cm = confusion_matrix(Y_test,Y_Pred)
print(cm)

print("Classification Report")
print(classification_report(Y_Pred,Y_test))
