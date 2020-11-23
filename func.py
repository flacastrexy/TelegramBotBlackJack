from telebot import types
import json

cards = {
    '1': "Туз♣️",      # крести
    '2': "Туз♦️",      # буби
    '3': "Туз♥️",      # черви
    '4': "Туз ♠️",     # пики
    '5': "Король♣️",   # крести
    '6': "Король♦️",   # буби
    '7': "Король♥️",   # черви
    '8': "Король ♠️",  # пики
    '9': "Дама♣️",  # крести
    '10': "Дама♦️",  # буби
    '11': "Дама♥️",  # черви
    '12': "Дама ♠️",  # пики
    '13': "Валет♣️",  # крести
    '14': "Валет♦️",  # буби
    '15': "Валет♥️",  # черви
    '16': "Валет ♠️",  # пики
    '17': "10♣️",  # крести
    '18': "10♦️",  # буби
    '19': "10♥️",  # черви
    '20': "10 ♠️",  # пики
    '21': "9♣️",  # крести
    '22': "9♦️",  # буби
    '23': "9♥️",  # черви
    '24': "9 ♠️",  # пики
    '25': "8♣️",  # крести
    '26': "8♦️",  # буби
    '27': "8♥️",  # черви
    '28': "8 ♠️",  # пики
    '29': "7♣️",  # крести
    '30': "7♦️",  # буби
    '31': "7♥️",  # черви
    '32': "7 ♠️",  # пики
    '33': "6♣️",  # крести
    '34': "6♦️",  # буби
    '35': "6♥️",  # черви
    '36': "6 ♠️",  # пики
    '37': "5♣️",  # крести
    '38': "5♦️",  # буби
    '39': "5♥️",  # черви
    '40': "5 ♠️",  # пики
    '41': "4♣️",  # крести
    '42': "4♦️",  # буби
    '43': "4♥️",  # черви
    '44': "4 ♠️",  # пики
    '45': "3♣️",  # крести
    '46': "3♦️",  # буби
    '47': "3♥️",  # черви
    '48': "3 ♠️",  # пики
    '49': "2♣️",  # крести
    '50': "2♦️",  # буби
    '51': "2♥️",  # черви
    '52': "2 ♠️",  # пики
}


def get_score_card(card):
    int(card)
    if (card >= 1) and (card <= 4):
        return 11
    elif (card >= 5) and (card <= 8):
        return 4
    elif (card >= 9) and (card <= 12):
        return 3
    elif (card >= 13) and (card <= 16):
        return 2
    elif (card >= 17) and (card <= 20):
        return 10
    elif (card >= 21) and (card <= 24):
        return 9
    elif (card >= 25) and (card <= 28):
        return 8
    elif (card >= 29) and (card <= 32):
        return 7
    elif (card >= 33) and (card <= 36):
        return 6
    elif (card >= 37) and (card <= 40):
        return 5
    elif (card >= 41) and (card <= 44):
        return 4
    elif (card >= 45) and (card <= 48):
        return 3
    else:
        return 2


def create_new_game_buttons():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Начать игру!🎮")
    markup.add(button1)
    return markup


def create_game_buttons():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Еще! 👍🏼")
    button2 = types.KeyboardButton("Стоп! ✋🏼")
    markup.add(button1, button2)
    return markup


def save(db):
    with open('data/bd.json', 'w') as outfile:
        json.dump(db, outfile)


def load():

  db = json.load(open("data/bd.json"))
  return db
