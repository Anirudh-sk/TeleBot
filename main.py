import os
import time
import telebot
import threading
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

bot = telebot.TeleBot(BOT_TOKEN)

my_variable = 0

def send_message_to_group(NFO, BuyPrice):
    global my_variable
    previous_value = None
    sl=BuyPrice-BuyPrice*0.12
    Target=BuyPrice+BuyPrice*0.15

    while True:
        if my_variable != previous_value:
            message_text = f"Buy {NFO} @ {BuyPrice} \n StopLoss {sl} \n Target {Target} "
            bot.send_message(chat_id=CHAT_ID, text=message_text)
            previous_value = my_variable

        time.sleep(5)  # Adjust the sleep interval as needed

def update_variable():
    global my_variable

    while my_variable != 2:
        my_variable += 1
        time.sleep(10)

send_message_thread = threading.Thread(target=send_message_to_group(NFO="Nifty 19900 CE", BuyPrice=80))
send_message_thread.daemon = True
send_message_thread.start()

update_variable_thread = threading.Thread(target=update_variable)
update_variable_thread.daemon = True
update_variable_thread.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

# def get_group_chat_id():
#     # Get updates from the bot
#     updates = bot.get_updates()
#     print("Updates:", updates)
    
#     # Check the latest update to get the chat ID of the group
#     if updates:
#         latest_update = updates[-1]
#         chat_id = latest_update.message.chat.id
#         print("Group Chat ID:", chat_id)
#     else:
#         print("No updates received yet. Make sure the bot is added to the group and try again.")

# get_group_chat_id()