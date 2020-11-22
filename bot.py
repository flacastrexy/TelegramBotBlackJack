import config
import telebot
import random
import func
import db
import json

bot = telebot.TeleBot(config.TOKEN)
db = db.db


# cards_now = []
# cards_croupier = []
# score = 0
# score_croupier = 0
# player_wins = 0


@bot.message_handler(commands=['start'])
def welcome(message):
    player_wins = 0
    hi_sticker = open('stickers/hi_21.webp', 'rb')
    bot.send_sticker(message.chat.id, hi_sticker)
    markup = func.create_new_game_buttons()
    bot.send_message(message.chat.id, "Привет, <b>{0.first_name}</b>!\nЯ бот для игры в <b>BlackJack</b>."
                                      "\nНу что приступим?".format(message.from_user, bot.get_me()), parse_mode='html',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.chat.type == 'private':
        global db
        if message.text == 'Начать игру!🎮':

            db = json.load(open("bd.json"))

            markup = func.create_game_buttons()
            if str(message.chat.id) not in db:
                db[str(message.chat.id)] = {
                    'cards_now': [],
                    'cards_croupier': [],
                    'score': 0,
                    'score_croupier': 0,
                    'wins': 0
                }
            else:
                db[str(message.chat.id)]['score'] = 0
                db[str(message.chat.id)]['score_croupier'] = 0
                db[str(message.chat.id)]['cards_now'] = []
                db[str(message.chat.id)]['cards_croupier'] = []

            json.dump(db, open("bd.json", "w"))

            # score = 0
            # score_croupier = 0

            # cards_now = []
            # cards_croupier = []

            random_card = random.randint(1, 52)
            random_croupier = random.randint(1, 52)

            db[str(message.chat.id)]['cards_now'].append(func.cards[str(random_card)])
            db[str(message.chat.id)]['cards_croupier'].append(func.cards[str(random_croupier)])

            # cards_now.append(func.cards[str(random_card)])
            # cards_croupier.append(func.cards[str(random_croupier)])

            db[str(message.chat.id)]['score'] += func.get_score_card(random_card)
            db[str(message.chat.id)]['score_croupier'] += func.get_score_card(random_croupier)

            # score += func.get_score_card(random_card)
            # score_croupier += func.get_score_card(random_croupier)

            bot.send_message(message.chat.id, "Ваши карты: " + ", ".join(db[str(message.chat.id)]['cards_now']) +
                             "\n Ваши очки:" + str(db[str(message.chat.id)]['score']),
                             reply_markup=markup)
        if message.text == 'Еще! 👍🏼':
            markup = func.create_game_buttons()

            random_card = random.randint(1, 52)
            random_croupier = random.randint(1, 52)

            db[str(message.chat.id)]['cards_now'].append(func.cards[str(random_card)])
            db[str(message.chat.id)]['cards_croupier'].append(func.cards[str(random_croupier)])

            # cards_now.append(func.cards[str(random_card)])
            # cards_croupier.append(func.cards[str(random_croupier)])

            db[str(message.chat.id)]['score'] += func.get_score_card(random_card)
            db[str(message.chat.id)]['score_croupier'] += func.get_score_card(random_croupier)

            # score += func.get_score_card(random_card)
            # score_croupier += func.get_score_card(random_croupier)

            bot.send_message(message.chat.id, "Ваши карты: " + ", ".join(db[str(message.chat.id)]['cards_now']) +
                             "\n Ваши очки:" + str(db[str(message.chat.id)]['score']),
                             reply_markup=markup)

            if db[str(message.chat.id)]['score'] > 21:
                markup = func.create_new_game_buttons()
                bot.send_message(message.chat.id, "Вы проиграли, попробуйте снова 😥\n Ваша статистика: " +
                                 str(db[str(message.chat.id)]['wins']), reply_markup=markup)

        if message.text == 'Стоп! ✋🏼':
            markup = func.create_new_game_buttons()

            bot.send_message(message.chat.id, "Карты крупье: " + ", ".join(db[str(message.chat.id)]['cards_croupier'])
                             + "\nОчки крупье:" +
                             str(db[str(message.chat.id)]['score_croupier']), reply_markup=markup)
            if db[str(message.chat.id)]['score_croupier'] > 21:
                score_new = 0

            else:
                score_new = db[str(message.chat.id)]['score_croupier']
            if db[str(message.chat.id)]['score'] > score_new:
                db[str(message.chat.id)]['wins'] += 1
                bot.send_message(message.chat.id, "Поздравляем! Вы выиграли! 👏🏻\nВаша статистика: "
                                 + str(db[str(message.chat.id)]['wins']))
                json.dump(db, open("bd.json", "w"))

            elif db[str(message.chat.id)]['score'] == score_new:
                bot.send_message(message.chat.id, "Ничья! 🧐")
            else:
                bot.send_message(message.chat.id, "Вы проиграли, попробуйте снова 😥")


bot.polling(none_stop=True)
