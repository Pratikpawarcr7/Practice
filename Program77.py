
def main():

    try :
        sobj = open("Marvellous.txt","w")

        sobj.write("Marvellous Infosystem Pune")

        print(sobj)

    except FileNotFoundError as fobj:
        print("File Not Found")

if __name__ == "__main__":
    main()
