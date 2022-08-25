import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'It\'s coffee time! ☕️', parse_mode='html')
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} Woof! Woof!\nI am <b>{bot.get_me().first_name}</b>, a bot designed to help you with coffee order ☕️', parse_mode='html')
    # bot.send_message(message.chat.id, 'Menu: <b>Cappucino</b>, <b>Espresso</b> and <b>Americano</b>', parse_mode='html')
    # bot.send_message(message.chat.id, 'Type <b>Sticker</b> to get our exclusive <b>StickerPack</b>', parse_mode='html')
    # bot.send_message(message.chat.id, 'I can send you 2 songs: <b>more</b> and <b>goona be alright</b>', parse_mode='html')
    # bot.send_message(message.chat.id, 'I can calculate gb of sended photo', parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)   
    start = types.KeyboardButton('/start')
    about = types.KeyboardButton('/about')
    website = types.KeyboardButton('/website')
    menu = types.KeyboardButton('/menu')
    coffeefm = types.KeyboardButton('/coffeefm')
    markup.add(start, about, website, coffeefm, menu)
    bot.send_message(message.chat.id, '⬇️ Check your button bar ⬇️', reply_markup=markup)

@bot.message_handler(commands=['back'])
def back(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)   
    start = types.KeyboardButton('/start')
    about = types.KeyboardButton('/about')
    website = types.KeyboardButton('/website')
    menu = types.KeyboardButton('/menu')
    markup.add(start, about, website, menu)
    bot.send_message(message.chat.id, '⬇️ Your button bar has been updated ⬇️', reply_markup=markup)

@bot.message_handler(commands=['coffeefm'])
def back(message):
    bot.send_message(message.chat.id, 'It\'s <b>CoffeeFM</b>, what can be better than listen to music while you drink a cup of your favorite coffee 🎶\n⬇️ Choose the Music below ⬇️', reply_markup=markup, parse_mode = 'html')
    bot.send_message(message.chat.id, '1️⃣ Kanye West - Closed on sunday\n2️⃣ Sweetbox - Gonna Be Alright\n3️⃣ Powfu - Death bed\n4️⃣ Cafe Con Leche - LoFi Coffee', reply_markup=markup, parse_mode = 'html')  
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)   
    one = types.KeyboardButton('1')
    two = types.KeyboardButton('2')
    three = types.KeyboardButton('3')
    four = types.KeyboardButton('4')
    markup.add(one, two, three, four)
    bot.send_message(message.chat.id, '⬇️ Your button bar has been updated ⬇️', reply_markup=markup)

@bot.message_handler(commands=['menu'])
def about(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True)
    cappuccino = types.KeyboardButton('Cappuccino')
    espresso = types.KeyboardButton('Espresso')
    americano = types.KeyboardButton('Americano')
    start = types.KeyboardButton('/back')
    markup.add(cappuccino, espresso, americano, start)
    bot.send_message(message.chat.id, '⬇️ Menu is now below ⬇️', reply_markup=markup)

@bot.message_handler(commands=['about'])
def about(message):
    bot.send_message(message.chat.id, 'The best man\'s friend and Coffee shop\'s lovely pet! 🐶❤️\nAlways ready to help you with order! Whoof!\n\n<b>Our Coffee</b> ☕️\nIt takes many hands to craft the perfect cup of coffee – from the farmers who tend to the red-ripe coffee cherries, to the master roasters who coax the best from every bean, and to the barista who serves it with care. We are committed to the highest standards of quality and service, embracing our heritage while innovating to create new experiences to savor.', parse_mode='html')

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Go to website', url='http://127.0.0.1:8000/'))
    bot.send_message(message.chat.id, '✨Check our website for more information and gifts!!!✨\n✨Find secret code and use it to get free coffee!!!✨', reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True)   
    back = types.KeyboardButton('/back')
    markup.add(back, back, back)
    bot.send_message(message.chat.id, '⬇️ We suggest you to come <b>back</b> ⬇️', reply_markup=markup, parse_mode = 'html')
    bot.send_message(message.chat.id, 'If you find any errors please contacts us\nOur email: nrsltnsdkv@gmail.com', parse_mode='html')


@bot.message_handler()
def send_user_text(message): 
    if message.text == 'hello' or message.text == 'hi' or message.text == 'Hello' or message.text == 'Hi':
        bot.send_message(message.chat.id, f'{message.text} to you too!', parse_mode = 'html')

    elif message.text == 'cappuccino' or message.text == 'Cappuccino':
        photo = open('/Users/nursultan/Desktop/telebot/static/fff1.jpeg', 'rb')
        desc = '<b>Cappuccino</b>\n\nDark, rich espresso lies in wait under a smoothed and stretched layer of thick milk foam. An alchemy of barista artistry and craft.\n\n140 calories, 12g sugar, 5g fat\n\nprice: $4.05'
        bot.send_photo(message.chat.id, photo, caption=desc, parse_mode = 'html')
    
    elif message.text == 'espresso' or message.text == 'Espresso':
        photo = open('/Users/nursultan/Desktop/telebot/static/fff2.jpeg', 'rb')
        desc = '<b>Espresso</b>\n\nOur smooth signature Espresso Roast with rich flavor and caramelly sweetness is at the very heart of everything we do.\n\n10 calories, 0g sugar, 0g fat\n\nprice: $2.35'
        bot.send_photo(message.chat.id, photo, caption=desc, parse_mode = 'html')

    elif message.text == 'americano' or message.text == 'Americano':
        photo = open('/Users/nursultan/Desktop/telebot/static/fff3.jpeg', 'rb')
        desc = '<b>Americano</b>\n\nEspresso shots topped with hot water create a light layer of crema culminating in this wonderfully rich cup with depth and nuance.\n\n15 calories, 0g sugar, 0g fat\n\nprice: $3.05'
        bot.send_photo(message.chat.id, photo, caption=desc, parse_mode = 'html')
    
    elif message.text == '1' or message.text == '1️⃣':
        audio = audio=open('/Users/nursultan/Desktop/telebot/static/Kanye West - Closed On Sunday Lp0q1wWe6XI.m4a', 'rb')
        bot.send_audio(message.chat.id, audio)

    elif message.text == '2' or message.text == '2️⃣':
        audio = audio=open('/Users/nursultan/Desktop/telebot/static/17  Sweetbox - Gonna Be Alright.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    
    elif message.text == '3' or message.text == '3️⃣':
        audio=open('/Users/nursultan/Desktop/telebot/static/Death bed coffee   Powfu.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    
    elif message.text == '4' or message.text == '4️⃣':
        audio=open('/Users/nursultan/Desktop/telebot/static/Cafe Con Leche - Lofi Coffee.m4a', 'rb')
        bot.send_audio(message.chat.id, audio)
    
    elif message.text == 'sticker' or message.text == 'Sticker':
        sticker=open('/Users/nursultan/Desktop/telebot/static/sticker.tgs', 'rb')
        bot.send_sticker(message.chat.id, sticker)
    
    else:
        bot.send_message(message.chat.id, 'I don\'understand you! 😕\nSend "/help" to get help', parse_mode='html')
    


# @bot.message_handler(content_types=['photo'])
# def get_user_photo(message):
#     bot.send_message(message.chat.id, 'Nice photo!')
#     bot.send_message(message.chat.id, f'{message.photo[-1].file_size} gb.')




#coffee fm - radio
#coffee stickers - stickers

bot.polling(none_stop=True)

