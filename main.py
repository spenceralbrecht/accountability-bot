import os
from twilio.rest import Client
from dotenv import load_dotenv
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables from the .env file
load_dotenv()

# Set up your Twilio API credentials
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_phone_number = os.environ['TWILIO_PHONE_NUMBER']
my_phone_number = os.environ['MY_PHONE_NUMBER']

# Initialize the Twilio client
client = Client(account_sid, auth_token)

def send_text_message():
    try:
        message = client.messages.create(
            body="What are your 3 biggest priorities for today?",
            from_=twilio_phone_number,
            to=my_phone_number
        )
        logging.info(f"Message sent: {message.sid}")
    except Exception as e:
        logging.error(f"Error sending message: {e}")

send_text_message()
