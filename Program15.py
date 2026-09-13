def main():

    try:
        fobj = open("Demo.txt","w")

        fobj.write("Marvellous Infosystem")

        print("Filed Gets Open Succesfully")

    except FileNotFoundError as fObj:
        print("File Not Found")

if __name__ == "__main__":
    main()