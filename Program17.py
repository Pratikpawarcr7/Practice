def main():

    try:
        fobj = open("Demo.txt","r")

        print("Filed Gets Open Succesfully")

        Data = fobj.read()

        print(Data)

    except FileNotFoundError as fObj:
        print("File Not Found")

if __name__ == "__main__":
    main()