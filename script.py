import telebot
from telebot import types

bot = telebot.TeleBot('8411699454:AAFtArqY1tFgz89qGK18JmWpMEbfXtNJihY')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        types.KeyboardButton('Завтрак'),
        types.KeyboardButton('Обед'),
        types.KeyboardButton('Ужин')
    )
    bot.send_message(message.chat.id, "Что готовим?", reply_markup=markup)

# Обработчик всех текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()

    if text == 'завтрак':
        breakfast_dishes = [
            "Блины", "Сырники", "Оладьи", "Яичница",
            "Рисовая каша", "Омлет", "Овсяная каша", "Вафли",
            "Скрэмбл", "Манная каша", "Творог", "Гречневая каша", "Шакшука"
        ]
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        for dish in breakfast_dishes:
            markup.add(types.KeyboardButton(dish))
        bot.send_message(message.chat.id, "Выберите блюдо на завтрак:", reply_markup=markup)

    elif text == 'обед':
        lunch_dishes = [
            "Минестроне", "Чечевичный суп", "Окрошка", "Врап",
            "Щавелевый суп", "Шаверма", "Гороховый суп", "Рыбный суп",
            "Томатный суп", "Картофельный крем-суп", "Салат"
        ]
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        for dish in lunch_dishes:
            markup.add(types.KeyboardButton(dish))
        bot.send_message(message.chat.id, "Выберите блюдо на обед:", reply_markup=markup)

    elif text == 'ужин':  # Исправлено: добавлен отступ
        dinner_dishes = [
            "Запеченная рыба", "Запеченное мясо", "Тушеная капуста", "Плов",
            "Болоньезе", "Шаверма", "Драники", "Соус томатный",
            "Котлеты", "Вафли", "Салат", "Пастуший пирог", "Лобио", "Оливье", "Поке", "Вок", "Стейк"
        ]
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        for dish in dinner_dishes:
            markup.add(types.KeyboardButton(dish))
        bot.send_message(message.chat.id, "Выберите блюдо на ужин:", reply_markup=markup)

# Запуск бота
bot.polling(none_stop=True)
