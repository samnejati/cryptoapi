import os
import telebot
from loguru import logger

telToken = os.environ['telegramToken']

bot = telebot.TeleBot(telToken)
logger.info('bot shoro shodeh...')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    logger.info("yeki az bot estefadeh kard!!!")
    bot.reply_to(message, "Salam, chetori??")

# write the code here:
@bot.message_handler(func=lambda message: True)
def welcome(message):
    bot.reply_to(message, message.text)
    
bot.infinity_polling()
