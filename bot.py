import telebot
from telebot import types
import random
from joke import a,stirlitz,c
bot = telebot.TeleBot("5688637604:AAHVPDci7bqsTWAz6p5hsM8-VphGBNZMi6o", parse_mode='HTML')

@bot.message_handler(commands=['start'])

def start(message):
	name =f'Привет, {message.from_user.first_name} <u>{message.from_user.last_name}</u>, Напиши слово "Юмор" '
	bot.send_message(message.chat.id,name)

# @bot.message_handler()
# def user_text(message):
# 	if message.text != "/start":
# 		bot.send_message(message.chat.id, "Напишите /start")


@bot.message_handler(content_types=['text'])
def joke(message):
	if message.text == 'Юмор' or message.text == 'юмор':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton('Анекдоты 1 категории')
		btn2 = types.KeyboardButton('Анекдоты 2 категории')
		btn3 = types.KeyboardButton('Анекдоты 3 категории')
		markup.add(btn1, btn2, btn3)
		bot.send_message(message.from_user.id, 'Выберие категорию анекдотов', reply_markup=markup)


	elif message.text == 'Анекдоты 1 категории':
		bot.send_message(message.from_user.id,random.choice(a))
	elif message.text == 'Анекдоты про штирлица':
		bot.send_message(message.from_user.id,random.choice(stirlitz))
	elif message.text == 'Анекдоты 3 категории':
		bot.send_message(message.from_user.id,random.choice(c))

bot.polling(none_stop=True)