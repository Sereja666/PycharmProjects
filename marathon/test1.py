from apscheduler.schedulers.background import BackgroundScheduler
from aiogram import Bot

token = "5483967327:AAHbSgzVqkhjZp52crKyTq__jREVnvShFM8"
bot = Bot(token)


def send_message():
    bot.send_message("334892317", "привет")


while True:
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_message, "interval", seconds=10)