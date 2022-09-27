import telebot
from telebot import types
from config import tokens
import re
bot = telebot.TeleBot(tokens['token'])

# команда-помощник
@bot.message_handler(commands=['start', 'help'])
def help(message):
    help_string = 'Это бот, который позволит Вам работать с запросамы.\n\n' \
                  'Введите запрос, либо выберите один из списка'\
                #   '<strong>Список команд</strong>\n' \
                #   '/orders - получить список активных заказов\n' \
                #   '/?  (? - код заказа) - получить заказ по его коду'

    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    item = types.KeyboardButton("Ввести свой запрос")
    item1 = types.KeyboardButton("from tbl_157224,join tbl_157223")
    item2 = types.KeyboardButton("from tbl_195789")
    markup.add(item)
    markup.add(item1)
    markup.add(item2)
    
    bot.send_message(message.chat.id, help_string, parse_mode='html', reply_markup= markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':

  
        if message.text == 'from tbl_157224,join tbl_157223':
            timeForRes = GetTime("from tbl_157224,join tbl_157223") 
            bot.send_message(message.chat.id, timeForRes, parse_mode='html')
        elif message.text == 'from tbl_195789':
            timeForRes = GetTime("from tbl_195789") 
            bot.send_message(message.chat.id, timeForRes, parse_mode='html')
        elif message.text == 'Ввести свой запрос':
            msg = bot.send_message(message.chat.id, 'Введите свой запрос:')
            bot.register_next_step_handler(msg, start_2)
            


def start_2(message):

    result = re.match(r"((from|into|join|INTO|JOIN|FROM)\stbl_(\d)*\,)*((from|into|join|INTO|JOIN|FROM)\stbl_(\d)*)", message.text)
    if result == None:
        bot.send_message(message.chat.id, "Ваш запрос не корректен", parse_mode='html')
    else:
        timeForRes = GetTime(message.text) 
        bot.send_message(message.chat.id, timeForRes, parse_mode='html')

def GetTime(response):
    time = "13 ms"
    ## Здесь происходит связь с МЛ - в  response - лежит запрос, а метод должен вернуть время его выполнения строкой
    return time



bot.polling(none_stop=True)