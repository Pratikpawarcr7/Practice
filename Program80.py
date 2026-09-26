
def main():

    try :
        sobj = open("Marvellous.txt","r")

        print("File Offset is : ",sobj.tell())
        Data = sobj.read(10)

        print(Data)

        print("File Offset is : ",sobj.tell())
        Data = sobj.read(10)
        
        print(Data)

        print("File Offset is : ",sobj.tell())
        Data = sobj.read(10)
                
        print(Data)

        sobj.close()

    except FileNotFoundError as fobj:
        print("File Not Found")

if __name__ == "__main__":
    main()
