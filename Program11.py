import time
import datetime
import schedule

def Display():

    print("Current Time : ",datetime.datetime.now())

def main():

    schedule.every(1).minute.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
    main()