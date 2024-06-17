import pandas as pd
import pywhatkit as kit
import schedule
import time
from datetime import datetime

def read_contacts(file_path):
    return pd.read_csv(file_path)

def read_template(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def send_message(phone, message):
    current_time = datetime.now()
    kit.sendwhatmsg(phone, message, current_time.hour, current_time.minute + 1)

def send_bulk_messages():
    contacts = read_contacts('contacts.csv')
    template = read_template('message_templates/template1.txt')
    
    for index, row in contacts.iterrows():
        personalized_message = template.format(name=row['name'])
        send_message(row['phone'], personalized_message)

schedule.every().day.at("09:00").do(send_bulk_messages)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
