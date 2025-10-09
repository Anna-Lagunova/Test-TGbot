import telebot
from telebot import types

bot = telebot.TeleBot('8411699454:AAFtArqY1tFgz89qGK18JmWpMEbfXtNJihY')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаем клавиатуру
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    
    # Создаем кнопки
    btn1 = types.KeyboardButton('Завтрак')
    btn2 = types.KeyboardButton('Обед')
    btn3 = types.KeyboardButton('Ужин')
    
    # Добавляем кнопки в клавиатуру
    markup.add(btn1, btn2, btn3)
    
    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Что готовим?", reply_markup=markup)

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text.lower() == 'завтрак':
        # Создаем клавиатуру для блюд на завтрак
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        
        # Список блюд для завтрака
        breakfast_dishes = [
            "Блины", "Сырники", "Оладья", "Яичница",
            "Рисовая каша", "Омлет", "Овсяная каша", "Вафли",
            "Скрэмбл", "Манная каша", "Творог", "Гречневая каша", "Шакшука"
        ]
        
        # Создаем кнопки для каждого блюда
        for dish in breakfast_dishes:
            markup.add(types.KeyboardButton(dish))

        # Список блюд для обеда
        lunch_dishes = [
            "Минестроне", "Чечевичный суп", "Окрошка", "Врап",
            "Щавелевый суп", "Шаверма", "Гороховый суп", "Рыбный суп",
            "Томатный суп", "Картофельный крем-суп", "Салат"
        ]
        # Создаем кнопки для каждого блюда
        for dish in lunch_dishes:
            markup.add(types.KeyboardButton(dish))

        # Список блюд для ужина
        dinner_dishes = [
            "Запеченная рыба", "Запеченное мясо", "Тушеная капуста", "Плов",
            "Болоньезе", "Шаверма", "Драники", "Соус томатный",
            "Котлеты", "Вафли", "Салат", "Пастуший пирог", "Лобио", "Оливье", "Поке", "Вок", "Стейк"
        ]
        # Создаем кнопки для каждого блюда
        for dish in dinner_dishes:
            markup.add(types.KeyboardButton(dish))
        # Добавляем кнопку "Назад"
        markup.add(types.KeyboardButton("Назад"))
        
        bot.send_message(message.chat.id, "Выберите блюдо на завтрак:", reply_markup=markup)
    
    
        bot.send_message(message.chat.id, "Выберите блюдо на обед:", reply_markup=markup)   
    
        bot.send_message(message.chat.id, "Выберите блюдо на ужин:", reply_markup=markup)
    
    elif message.text.lower() == 'назад':
        # Возвращаемся к главному меню
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

# Запуск бота
if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()
