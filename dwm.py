# Наговнокоддено и защищенно правом Ametero(z)
import telebot # Для функции управления с помощью ТГ
from telebot import types # Для функции управления с помощью ТГ
import winsound # Проигрывание .wav файлов
import pyvolume # Библиотека для изменения уровня громкости

# Говнокодинный вирусс прикол пранк Барбарики
# Надеюсь прочитал сам гитхаб поэтому вопросов мало
# Форкнуто с кода MrDimon, отличия по коду есть, но они удаляют не нужные функции

bot = telebot.TeleBot('хихихи') # Токен для бота лол

@bot.message_handler(commands=['start'])
def start(message):
        user = message.from_user.id
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # Размечаем клаву
        btn1 = types.KeyboardButton('Барбарики))')
        markup.add(btn1)
        bot.send_message(user, 'Сделанно по мысле от Яноть\nФоркнутый вирус\nДля краша скрипта используйте /crash', reply_markup=markup)
@bot.message_handler(commands=['crash']) # Команда для краша скрипта
def crash(message):
     user = message.from_user.id
     bot.send_message(user, "Скрипт крашится")
     quit()

@bot.message_handler(content_types=['text']) # Функционал кнопок
def get_text_messages(message):
     user = message.from_user.id
     if message.text == "Барбарики))": # Включение барбариков
          bot.send_message(user, "Включаем звук")
          pyvolume.custom(100)
          bot.send_message(user, "Включаем барбариков")
          winsound.PlaySound('br.wav', winsound.SND_FILENAME)
          bot.send_message(user, "Барбарики успокоились)")

bot.polling() # Поллинг бота
