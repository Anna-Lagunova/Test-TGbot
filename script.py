import os
import telebot
from telebot import types

# Получаем токен из переменных окружения (для безопасности)
BOT_TOKEN = os.environ.get('BOT_TOKEN') or '8411699454:AAFtArqY1tFgz89qGK18JmWpMEbfXtNJihY'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('завтрак')
    btn2 = types.KeyboardButton('обед')
    btn3 = types.KeyboardButton('ужин')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Выберите прием пищи:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text.lower() == 'завтрак':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        breakfast_dishes = [
            "блинчики", "сырники", "оладушки", "яичница",
            "рисовая каша", "омлет", "овсяная каша", "вафли",
            "скрэмбл", "манная каша", "творог", "гречневая каша", "шакшука"
        ]
        for dish in breakfast_dishes:
            markup.add(types.KeyboardButton(dish))
        markup.add(types.KeyboardButton("Назад"))
        bot.send_message(message.chat.id, "Выберите блюдо на завтрак:", reply_markup=markup)
    
    elif message.text.lower() == 'обед':
        bot.send_message(message.chat.id, "Функционал для обеда в разработке")
    
    elif message.text.lower() == 'ужин':
        bot.send_message(message.chat.id, "Функционал для ужина в разработке")
    
    elif message.text.lower() == 'назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('завтрак')
        btn2 = types.KeyboardButton('обед')
        btn3 = types.KeyboardButton('ужин')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "Выберите прием пищи:", reply_markup=markup)
    
    elif message.text.lower() in ["блинчики", "сырники", "оладушки", "яичница", 
                                 "рисовая каша", "омлет", "овсяная каша", "вафли",
                                 "скрэмбл", "манная каша", "творог", "гречневая каша", "шакшука"]:
        bot.send_message(message.chat.id, f"Вы выбрали: {message.text}\nПриятного аппетита!")

if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()
