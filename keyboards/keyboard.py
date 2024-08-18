from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

remove_menu = ReplyKeyboardRemove(selective=True)

def get_language_manu() -> ReplyKeyboardMarkup:
    language_manu = ReplyKeyboardMarkup(resize_keyboard=True)

    uz = KeyboardButton("Uzbek tili")
    ru = KeyboardButton("Rus tili")
    en = KeyboardButton("Ingliz tili")
    language_manu.add(uz, ru)
    language_manu.add(en)

    return language_manu

def get_ask_manu() -> ReplyKeyboardMarkup:
    ask_manu = ReplyKeyboardMarkup(resize_keyboard=True)

    yes = KeyboardButton("Ha")
    no = KeyboardButton("Yo'q")
    ask_manu.add(yes, no)

    return ask_manu

def get_buged_manu() -> ReplyKeyboardMarkup:
    buged_manu = ReplyKeyboardMarkup(resize_keyboard=True)

    one = KeyboardButton("100$ dan 500$ gacha")
    two = KeyboardButton("500$ dan 1,000$ gacha")
    three = KeyboardButton("1,000$ dan 2,500$ gacha")
    buged_manu.add(one, two)
    buged_manu.add(three)

    return buged_manu

def get_contact_manu() -> ReplyKeyboardMarkup:
    contact_manu = ReplyKeyboardMarkup(resize_keyboard=True)

    contact = KeyboardButton("Raqam yuborish!", request_contact=True)
    contact_manu.add(contact)

    return contact_manu
