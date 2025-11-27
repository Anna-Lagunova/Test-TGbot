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

# Обработчик для выбора типа приема пищи
@bot.message_handler(func=lambda message: message.text.lower() in ['завтрак', 'обед', 'ужин'])
def handle_meal_choice(message):
    text = message.text.lower()

    if text == 'завтрак':
        breakfast_dishes = [
            "Блины", "Сырники", "Оладьи", "Яичница",
            "Рисовая каша", "Омлет", "Овсяная каша", "Вафли",
            "Скрэмбл", "Манная каша", "Творог", "Гречневая каша", "Шакшука"
        ]
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        # Добавляем кнопку "Назад" для возврата к выбору приема пищи
        for i in range(0, len(breakfast_dishes), 2):
            if i + 1 < len(breakfast_dishes):
                markup.row(breakfast_dishes[i], breakfast_dishes[i + 1])
            else:
                markup.row(breakfast_dishes[i])
        markup.row(types.KeyboardButton('Назад'))
        bot.send_message(message.chat.id, "Выберите блюдо на завтрак:", reply_markup=markup)

    elif text == 'обед':
        lunch_dishes = [
            "Минестроне", "Чечевичный суп", "Окрошка", "Врап",
            "Щавелевый суп", "Шаверма", "Гороховый суп", "Рыбный суп",
            "Томатный суп", "Картофельный крем-суп", "Салат"
        ]
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        for i in range(0, len(lunch_dishes), 2):
            if i + 1 < len(lunch_dishes):
                markup.row(lunch_dishes[i], lunch_dishes[i + 1])
            else:
                markup.row(lunch_dishes[i])
        markup.row(types.KeyboardButton('Назад'))
        bot.send_message(message.chat.id, "Выберите блюдо на обед:", reply_markup=markup)

    elif text == 'ужин':
        dinner_dishes = [
            "Запеченная рыба", "Запеченное мясо", "Тушеная капуста", "Плов",
            "Болоньезе", "Шаверма", "Драники", "Соус томатный",
            "Котлеты", "Вафли", "Салат", "Пастуший пирог", "Лобио", "Оливье", "Поке", "Вок", "Стейк"
        ]
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        for i in range(0, len(dinner_dishes), 2):
            if i + 1 < len(dinner_dishes):
                markup.row(dinner_dishes[i], dinner_dishes[i + 1])
            else:
                markup.row(dinner_dishes[i])
        markup.row(types.KeyboardButton('Назад'))
        bot.send_message(message.chat.id, "Выберите блюдо на ужин:", reply_markup=markup)

# Обработчик для выбора конкретного блюда
@bot.message_handler(func=lambda message: message.text.lower() in [
    'блины', 'сырники', 'оладьи', 'яичница', 'рисовая каша', 'омлет', 'овсяная каша', 'вафли',
    'скрэмбл', 'манная каша', 'творог', 'гречневая каша', 'шакшука', 'минестроне', 'чечевичный суп',
    'окрошка', 'врап', 'щавелевый суп', 'шаверма', 'гороховый суп', 'рыбный суп', 'томатный суп',
    'картофельный крем-суп', 'салат', 'запеченная рыба', 'запеченное мясо', 'тушеная капуста', 'плов',
    'болоньезе', 'драники', 'соус томатный', 'котлеты', 'пастуший пирог', 'лобио', 'оливье', 'поке',
    'вок', 'стейк'
])
def handle_dish_choice(message):
    dish = message.text
    bot.send_message(message.chat.id, f"Отличный выбор! Готовим: {dish}")

# Обработчик для кнопки "Назад"
@bot.message_handler(func=lambda message: message.text.lower() == 'назад')
def handle_back(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        types.KeyboardButton('Завтрак'),
        types.KeyboardButton('Обед'),
        types.KeyboardButton('Ужин')
    )
    bot.send_message(message.chat.id, "Что готовим?", reply_markup=markup)

# Обработчик для всех остальных сообщений
@bot.message_handler(func=lambda message: True)
def handle_other_messages(message):
    bot.send_message(message.chat.id, "Пожалуйста, используйте кнопки для выбора.")

# Запуск бота
bot.polling(none_stop=True)
