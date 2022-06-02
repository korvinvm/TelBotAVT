print ("start script")
import telebot
from config import token
from telebot import types
print ("import Ok") 
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)
bot.infinity_polling()
print ("all Ok") 