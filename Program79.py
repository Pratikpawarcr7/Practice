
def main():

    try :
        sobj = open("Marvellous.txt","r")

        Data = sobj.read()

        print(Data)

        sobj.close()

    except FileNotFoundError as fobj:
        print("File Not Found")

if __name__ == "__main__":
    main()
