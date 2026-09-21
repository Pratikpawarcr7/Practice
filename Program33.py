
def main():
    try:

        fobj = open("Marvellous.txt","r")

       
        Data = fobj.read(6)

        print(Data)

        fobj.close()


    except FileNotFoundError as fobj:
        print("File Not Found")

if __name__ == "__main__":
    main()