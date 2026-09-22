import pandas as pd

def main():

   Data = {
       "Name" : ["Pratik","Pranay","Rohan"],
       "Age" : [21,22,23],
       "Salary" : [100000,20000,30000]
   }

   sobj = pd.DataFrame(Data)

   print(sobj)

   print(sobj[["Name","Age"]])
if __name__ == "__main__":
    main()  