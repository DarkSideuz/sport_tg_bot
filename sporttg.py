import telebot

API_TOKEN = 'TOKEN'
bot = telebot.TeleBot(API_TOKEN)

athletes = {
    "boks": ["Sportchi1", "Sportchi2", "Sportchi3"],
    "kurash": ["Sportchi4", "Sportchi5", "Sportchi6"],
    "shaxmat": ["Sportchi7", "Sportchi8", "Sportchi9"]
}

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, "Assalomu alaykum! Sport turini tanlang: /boks, /kurash, /shaxmat")

@bot.message_handler(commands=['boks'])
def boks_command(message):
    bot.reply_to(message, ", ".join(athletes['boks']))


@bot.message_handler(commands=['kurash'])
def kurash_command(message):
    bot.reply_to(message, ", ".join(athletes['kurash']))

@bot.message_handler(commands=['shaxmat'])
def shaxmat_command(message):
    bot.reply_to(message, ", ".join(athletes['shaxmat']))

bot.polling()
