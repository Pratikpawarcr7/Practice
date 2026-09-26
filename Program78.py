
def main():

    try :
        sobj = open("Marvellous.txt","r")

        Data = sobj.read(10)

        print(Data)

        sobj.close()

    except FileNotFoundError as fobj:
        print("File Not Found")

if __name__ == "__main__":
    main()
