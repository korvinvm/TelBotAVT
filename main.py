print ("start script")
import telebot
from config import token
from telebot import types
print ("import Ok") 
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")

#add button
@bot.message_handler(commands = ['url'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Наш сайт', url='https://habrahabr.ru')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Нажми на кнопку и перейди на наш сайт.", reply_markup = markup)

#@bot.send_message( )
#@bot.message_handler(func=lambda m: True)
#def echo_all(message):
#	bot.reply_to(message, message.text)
bot.infinity_polling()
print ("all Ok") 