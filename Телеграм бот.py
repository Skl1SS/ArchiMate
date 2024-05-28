import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler (commands=['start'])
def welcome(message):

    #Клавиатура
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Insert your business process description')
    item2 = types.KeyboardButton('Let\'s talk!')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Hello, {0.first_name}!\nI am <b>{1.first_name}</b>, bot made to convert your business project description into .archimate filetype models.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)  # <b> </b> Выделение жирным шрифтом части текста (b - bold)


@bot.message_handler (content_types=['text'])
def lalala(message):
    #бот повторяет написанное ему bot.send_message(message.chat.id, message.text)
    if message.chat.type == 'private':
        if message.text == 'Insert your business process description':
            bot.send_message(message.chat.id,'Type in your business process description, please')
        elif message.text == "Let's talk!":

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Where is my file?', callback_data='variant1')
            item2 = types.InlineKeyboardButton('I want my file', callback_data='variant2')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, "I wasn't made for talking!", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Your business model is ready to download\n https://konspekta.net/poisk-ruru/baza16/1953900495339.files/image012.jpg")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'variant1':
                bot.send_message(call.message.chat.id, 'I apologise, wait a little bit more')
            elif call.data == 'variant2':
                bot.send_message(call.message.chat.id, 'I\'m tired...')
            #Убрать кнопки клавиатуры под текстом бота
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Let's talk!",
                reply_markup=None)

            #Показать текстовое сообщение на весь экран
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                text='Bot is being developed')

    except Exception as e:
        print(repr(e))
#RUN
bot.polling(none_stop=True)


