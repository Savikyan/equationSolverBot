import telebot
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
API_TOKEN = '7846001329:AAGVTzk8JROCbVOcvNDQyt6EGAc3bqkAbf4'
bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт, я бот")


# # Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, message.text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bot.infinity_polling()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
