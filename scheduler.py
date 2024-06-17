import schedule
import time
from main import send_bulk_messages

schedule.every().day.at("09:00").do(send_bulk_messages)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
