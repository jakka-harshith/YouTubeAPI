import schedule
import time
import os

def job():
    os.system('python yt.py 200')
    print("yt.py script is run successfully")

# schedule.every(1).minutes.do(job)
# schedule.every().hour.do(job)
schedule.every().day.at("00:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)