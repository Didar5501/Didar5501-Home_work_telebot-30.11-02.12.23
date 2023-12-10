import telebot
import os
from telebot import types

TOKEN = '6543736032:AAHNWHo7l9qixS46YRFs8IfSeTMh35Raeok'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['dog'])
def send_dog_picture(message):
    dog_image_path = 'dog.jpeg'
    if os.path.exists(dog_image_path):
        with open(dog_image_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, 'Извините, не удалось найти изображение собаки.')


@bot.message_handler(commands=['start'])
def start(message):

    markup = types.InlineKeyboardMarkup()
    
    github_button = types.InlineKeyboardButton("github", url="https://github.com")
    markup.add(github_button)
    
 
    balance_button = types.InlineKeyboardButton("Баланс", callback_data="Баланс")
    markup.add(balance_button)
    
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

@bot.callback_query_handler(lambda call: call.data == "Баланс")
def balance_callback(query):
    send_balance_keyboard(query.message.chat.id)

@bot.callback_query_handler(lambda call: call.data == "Вывод")
def withdraw_callback(query):
    bot.send_message(query.message.chat.id, "Вы выбрали 'вывод'")

@bot.callback_query_handler(lambda call: call.data == "Пополнить")
def topup_callback(query):
    bot.send_message(query.message.chat.id, "Вы выбрали 'пополнить'")

def send_balance_keyboard(chat_id):
    markup = types.InlineKeyboardMarkup()
    
    withdraw_button = types.InlineKeyboardButton("вывод", callback_data="Вывод")
    markup.add(withdraw_button)
    
    topup_button = types.InlineKeyboardButton("пополнить", callback_data="Пополнить")
    markup.add(topup_button)
    
    bot.send_message(chat_id, "Выберите действие для баланса:", reply_markup=markup)

if __name__ == '__main__':
    bot.polling(none_stop=True)