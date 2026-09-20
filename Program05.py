import sys
import datetime
import schedule
import time

def Marvellous():

		print("Jay Ganesh...",datetime.datetime.now())

def main():

	schedule.every(1).minutes.do(Marvellous)

	while True:

		schedule.run_pending()
		time.sleep(10)

if __name__ == "__main__":

	main()
