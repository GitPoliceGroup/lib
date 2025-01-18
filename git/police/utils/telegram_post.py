import asyncio
import aiohttp
from dotenv import load_dotenv
import os

class AsynchronousTasker:
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.tasks = set()

    async def async_task_creator(self, callback, args):
        task = asyncio.create_task(callback(args))
        self.tasks.add(task)
        try:
            await task
            print("Sent message to telegram channel")
        finally:
            self.tasks.remove(task)

    def run_task(self, callback, args):
        task = self.loop.create_task(self.async_task_creator(callback, args))
        return task

class Telegram_Broadcaster:
    def __init__(self):
        load_dotenv()
        self.bot_token = os.environ['BOT_TOKEN']
        self.channel_id = os.environ['CHANNEL_ID']  
        self.base_url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage?chat_id={self.channel_id}"
        self.tasker = AsynchronousTasker()

    async def broadcast_message(self, message):
        url = self.base_url + f"&text={message}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                await response.text()  # For demonstration purposes

    def send_message(self, message):
        task = self.tasker.run_task(self.broadcast_message, message)
        return task

async def tele_broadcast_runner(message):
    myTG = Telegram_Broadcaster()
    task = myTG.send_message(message)
    print("Done")  # This will print immediately
    await task  # Wait for the message to be sent

def broadcast(message):
    asyncio.run(tele_broadcast_runner(message))

if __name__ == "__main__":
    broadcast("Test")
    