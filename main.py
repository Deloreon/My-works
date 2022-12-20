import telebot
import random
from env import token

bot = telebot.TeleBot(token)
keyboard = telebot.types.ReplyKeyboardMarkup()
button1 = telebot.types.KeyboardButton('Да')
button2 = telebot.types.KeyboardButton('Нет')
keyboard.add(button1,button2)



@bot.message_handler(commands = ['start', 'hi'])

def start_function(message):
    message = bot.send_message(message.chat.id ,f'Здраствуйте {message.chat.first_name} начнем игру?', reply_markup=keyboard)
    bot.register_next_step_handler(message, answer_check)
    # bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAJKJmOhPWxaQoQYDPotUmHnqmjCo-zaAAJaAAPANk8TC_wPT9xGGeEsBA')
    # bot.send_photo(message.chat.id, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsHrRWiABdVITNQDeXScYzuq0eAV_mgAitjg&usqp=CAU')
def answer_check(message):
    if message.text == 'Да':
        bot.send_message(message.chat.id, 'У тебя есть 3 попытки чтобы угадать число от 1 до 10')
        random_number = random.randint(1,10)
        p = 3
        start_game(message, random_number,p)
    else:
        bot.send_message(message.chat.id, 'Ну и ладно')

def start_game(message, random_number, p):
    message = bot.send_message(message.chat.id, 'Введи сичло от 1 до 10:')
    bot.register_next_step_handler(message, check_func, random_number, p-1)

def check_func(message, random_number, p):
    if message.text == str(random_number):
        bot.send_message(message.chat.id, 'Вы победли')
    elif p == 0:
        bot.send_message(message.chat.id, f'Вы проиграли! , Число было - {random_number}')
    else:
        bot.send_message(message.chat.id, f'Попробуй еще раз, у тебя осталось {p} попыток')
        start_game(message,random_number,p)
# @bot.message_handler()
# def echo_all(message):
#     bot.send_message(message.chat.id, message.text) 
bot.polling() # Позволяет запустить бота

