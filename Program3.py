import sys

def main():

	Border = "="*60

	print(Border)
	print("==================Marvellous AutoMation Script==================")
	print(Border)
	
	if(len(sys.argv) == 2):

		if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):

			print("Usage")

		elif(sys.argv[1] == "--h" or sys.argv[1] == "--H"):

			print("Help")

		else:

			DirectoryName = sys.argv[1]

			print("Directory Name : ",DirectoryName)

	else:

		print("Invalid Number Of Arguments")
		print("For More Information Please Enter the --h or --u")



	print(Border)
	print("==================Thanks For Using Marvellous AutoMation Script==================")
	print(Border)

if __name__ == "__main__":

	main()