from django.core.management.base import BaseCommand 
import telebot
from shop.models import Library

bot = telebot.TeleBot("6555950988:AAHJ-PInrF7WWifcevDdBVaIRj3cteZp7KI") # Вставьте сюда свой токен

@bot.message_handler(commands=['start']) 
def start(message):
    bot.send_message(message.chat.id, "Hello world!")

@bot.message_handler(commands=['libraries'])
def libraries(message):
    libraries = Library.objects.all()
    if libraries:
        response_message = "Available libraries and their book counts:\n"
        for library in libraries:
            response_message += f"{library.name} ({library.location}): {library.count_of_books} books\n"
    else:
        response_message = "No libraries available."

    bot.send_message(message.chat.id, response_message)

@bot.message_handler(commands=['help'])
def help(message):
    response_message = "Available commands:\n"
    response_message += "/start - Start the bot\n"
    response_message += "/libraries - List available libraries and their book counts\n"
    response_message += "/help - Show this help message"

    bot.send_message(message.chat.id, response_message)

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...") 
        bot.polling()
        print("Bot stopped")

@bot.message_handler(func=lambda message: True) 
def echo_all(message):
    bot.reply_to(message, message.text)