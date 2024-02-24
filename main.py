import telebot
from telebot import types

bot = telebot.TeleBot('6875484395:AAFTmuPr8hAoNkwr560S8uNOu6Sc5h1kopc')
@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет <b>{message.from_user.first_name} </b> крико друг'
    bot.send_message(message.chat.id, mess,  parse_mode='html')

# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == 'Hello':
#         bot.send_message(message.chat.id,"И тебе привет!", parse_mode='html')
#     elif message.text=='id':
#         bot.send_message(message.chat.id, f"Твой ID:{message.from_user.id}", parse_mode='html')
#     elif message.text == 'photo':
#         photo = open('untitled.png', 'rb')
#         bot.send_photo(message.chat.id, photo )
#     else:
#         bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Вау, крутая фотка бейби')


@bot.message_handler(commands=['website'])
def website (message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('напиши создателю бота что он крут чувак', 'https://vk.com/jjsgsif'))
    bot.send_message(message.chat.id, 'Перейди в вк броу', reply_markup=markup)

@bot.message_handler(commands=['help'])
def website (message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton("вот создатель")
    start = types.KeyboardButton('Стартуем')

    markup.add(website,start)
    bot.send_message(message.chat.id, 'напиши создателю бота что он крут чувак', reply_markup=markup)




bot.polling(non_stop=True)

