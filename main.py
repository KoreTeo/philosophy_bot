import csv
import random

import telebot

quotes = []
biography = []

with open('quotes.csv', encoding='UTF8') as f:
    reader = csv.reader(f)
    for row in reader:
        quotes += row

with open('biography.csv', encoding='UTF8') as f:
    reader = csv.reader(f)
    for row in reader:
        biography += row

bot = telebot.TeleBot('7069976868:AAH2IabI57xUIfjopSJYOZPxdh-k0yq_WgQ')

count_biography = 0


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.from_user.id,
        "Никколо́ ди Берна́рдо Макиаве́лли — итальянский мыслитель, политический деятель, философ, писатель, автор военно-теоретических трудов. Макиавелли часто считают отцом современной политической философии и политологии.\nВ данном боте вы можете получить информацию о философе, а также одну из его цитат",
        parse_mode='Markdown'
    )
    bot.send_message(
        message.from_user.id,
        'Меню:\n/biography - прочитать подробную биографию\n/quote - прочитать случайную цитату',
        parse_mode='Markdown'
    )


@bot.message_handler(commands=['biography'])
def get_text_messages(message):
    global count_biography
    bot.send_message(
        message.from_user.id,
        biography[count_biography],
        parse_mode='Markdown'
    )
    count_biography += 1
    bot.send_message(
        message.from_user.id,
        'Меню:\n/next - прочитать следующую часть\n/back - вернутся в меню',
        parse_mode='Markdown'
    )
    bot.delete_message(
        message.from_user.id,
        message.message_id - 1
    )


@bot.message_handler(commands=['quote'])
def send_quote(message):
    i = random.randint(0, 99)
    bot.send_message(
        message.from_user.id,
        quotes[i],
        parse_mode='Markdown'
    )
    bot.delete_message(
        message.from_user.id,
        message.message_id - 1
    )
    bot.send_message(
        message.from_user.id,
        'Меню:\n/biography - прочитать подробную биографию\n/quote - прочитать случайную цитату',
        parse_mode='Markdown'
    )


@bot.message_handler(commands=['next'])
def biography_next_text_messages(message):
    global count_biography
    if count_biography >= len(biography):
        bot.send_message(
            message.from_user.id,
            'Это последняя часть',
            parse_mode='Markdown'
        )
        count_biography = 0
        bot.delete_message(message.from_user.id, message.message_id - 1)
        bot.send_message(
            message.from_user.id,
            'Меню:\n/biography - прочитать подробную биографию\n/quote - прочитать случайную цитату',
            parse_mode='Markdown'
        )
    else:
        bot.send_message(
            message.from_user.id,
            biography[count_biography],
            parse_mode='Markdown'
        )
        bot.send_message(
            message.from_user.id,
            'Меню:\n/next - прочитать следующую часть\n/back - вернутся в меню',
            parse_mode='Markdown'
        )
        count_biography += 1
        bot.delete_message(message.from_user.id, message.message_id - 1)


@bot.message_handler(commands=['back'])
def biography_back_text_messages(message):
    bot.send_message(
        message.from_user.id,
        'Меню:\n/biography - прочитать подробную биографию\n/quote - прочитать случайную цитату',
        parse_mode='Markdown'
    )
    bot.delete_message(
        message.from_user.id,
        message.message_id - 1
    )


bot.polling(none_stop=True, interval=0)