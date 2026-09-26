
def main():

    try :
        sobj = open("Marvellous.txt","r")

        sobj.seek(10,0)

        Data = sobj.read()

        print(Data)

        sobj.close()

    except FileNotFoundError as fobj:
        print("File Not Found")

if __name__ == "__main__":
    main()
