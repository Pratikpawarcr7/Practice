def main():

    try:
        open("Demo.txt","r")

        print("Filed Gets Open Succesfully")

    except FileNotFoundError as fObj:
        print("File Not Found")

if __name__ == "__main__":
    main()