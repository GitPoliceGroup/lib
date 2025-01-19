import requests
import os
import asyncio
from dotenv import load_dotenv


# You can just import tg_post_bot and run send_message
# This will be executed in the background asynchronously, if all other programs end, the background task will persist till completion

class Telegram_Broadcaster:
    def __init__(self):
        load_dotenv()
        self.bot_token = os.environ['BOT_TOKEN']
        self.channel_id = os.environ['CHANNEL_ID']  
        self.base_url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage?chat_id={self.channel_id}"

    async def broadcast_message(self, message):
        url = self.base_url + f"&text={message}"
        requests.get(url)

    async def broadcast_message_asynchronously(self, message):
        task = asyncio.create_task(self.broadcast_message(message))
        print("Sent message to telegram channel")

    def send_message(self, message):
        asyncio.run(self.broadcast_message_asynchronously(message))

tg_post_bot = Telegram_Broadcaster() 

def send_telegram_message(message):
    tg_post_bot.send_message(message)

# if __name__ == "__main__":
#     tg_post_bot.send_message("Test")