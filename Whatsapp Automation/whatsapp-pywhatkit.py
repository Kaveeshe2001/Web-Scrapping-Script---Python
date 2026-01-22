import pywhatkit
from datetime import datetime, timedelta

phone_number = input("Enter the recipient's phone number (with country code): ")

# Schedule message 1 minute from now
now = datetime.now() + timedelta(minutes=1)

hour = now.hour
minute = now.minute

pywhatkit.sendwhatmsg(phone_number, "This is the automatically entered bot message. Don't take it seriously. You are the testing PAKAYA", hour, minute, wait_time=25, tab_close=True)