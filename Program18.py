def main():

    try:

        fobj = open("Demo.txt","r")
        print("File gets Opened")

        print("File offset is : ",fobj.tell())
        Data = fobj.read(2) 

        print(Data)

        print("File offset is : ",fobj.tell())
        Data = fobj.read() 
        
        print(Data)
        
        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not Present in Current Directory")

if __name__ == "__main__":
    main()

