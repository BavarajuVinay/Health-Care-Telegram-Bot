from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import requests
from bs4 import BeautifulSoup

v = "Please is not a valid medicine name"

updater = Updater("5965903649:AAF437FIdzMigvXoBKqG7mpvGDXvwG3uNQc",
				use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Hello sir, Welcome to the Bot.Please write\
		/help to see the commands available.")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/janaushadhi - To get the Government website URL
	/pharmaceuticals - To get the government pharmaceuticals URL
	/fluttertoindia - To get government fluttertoindia URL
	/genericure - To get the GeeksforGeeks URL""")


def janaushadhi_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Your janaushadhi link here (http://www.janaushadhi.gov.in/)")


def pharmaceuticals_url(update: Update, context: CallbackContext):
	update.message.reply_text("Pharmaceuticals website Link =>\
	https://www.pharmaceuticals.gov.in/")


def fluttertoindia_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"fluttertoindia URL => \
		https://www.fullertonindia.com/knowledge-center/pradhan-mantri-jan-aushadhi-kendra.aspx")


def genericure_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Genericure URL => https://www.genericure.in/")

def abcd(user_input):
    ip=user_input
    url='https://www.google.com/search?q='+ip+" uses"
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    page=requests.get(url,headers=headers)
    obj=BeautifulSoup(page.content,'html.parser')
    res=obj.find(class_='LGOjhe').get_text()
    return res

def reply(update: Update, context: CallbackContext):
    user_input=update.message.text
    update.message.reply_text(abcd(user_input))


def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('janaushadhi', janaushadhi_url))
updater.dispatcher.add_handler(CommandHandler('pharmaceuticals', pharmaceuticals_url))
updater.dispatcher.add_handler(CommandHandler('fluttertoindia', fluttertoindia_url))
updater.dispatcher.add_handler(CommandHandler('genericure', genericure_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, reply))

# Filters out unknown messages.

updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
