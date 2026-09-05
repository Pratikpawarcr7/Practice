import sys

def main():
	
	if(len(sys.argv) == 2):

		DirctoryName = sys.argv[1]
		print("Directory Name : ",DirctoryName)

	else:

		print("Invalid Number Of Arguments")

if __name__ == "__main__":

	main()