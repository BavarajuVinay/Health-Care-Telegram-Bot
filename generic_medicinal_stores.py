from telegram.update import Update
from telegram.ext.updater import Updater
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

from hos import my_data

v = []
b = ""
bii = "Invalid District,please try entering districts of A.P"

updater = Updater('5633741085:AAEuAbkhJ3d0UsvbVbdJlphxx4sCH5ji3n0', use_context=True) #

user_api = 'd91a74f331bbb8b424b920304262c616'

def start(update: Update, context: CallbackContext):
    update.message.reply_text(f"Welcome to the GENERIC_STORES_DATA_BOT\nPlease enter/"
                              f" /help if you want to more about about this bot")

def help(update: Update, context: CallbackContext):
    update.message.reply_text("Hello sir, Welcome to the Bot.Please write\
         /national_portal_of_india / \
            /National_Health_Authority /Health_Insurance_Subsidies\
                /HEALTHCARE_SCHEMES /National_institute_of_health and type the district for medical strores and their locations to see the commands available.")


def npoi(update: Update, context: CallbackContext):
    update.message.reply_text(f"national portal of india \nhttps://www.india.gov.in/")


def e_health(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"E-HEALTH & TELEMEDICINE \nhttps://www.main.mohfw.gov.in/Organisation/departments-health-and-family-welfare/e-Health-Telemedicine")


def National_Health_Authority(update: Update, context: CallbackContext):
    update.message.reply_text(f"National Health Authority \nhttps://hpr.ndhm.gov.in/en")


def Health_Insurance_Subsidies(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"Health Insurance Subsidies \nhttps://www.anthem.com/individual-and-family/insurance-basics/health-insurance/subsidy")


def HEALTHCARE_SCHEMES(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"HEALTHCARE SCHEMES \nhttps://www.moh.gov.sg/cost-financing/healthcare-schemes-subsidies")


def National_institute_of_health(update: Update, context: CallbackContext):
    update.message.reply_text(f"National_institute_of_health \nhttps://www.nih.gov/")


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)


def do_something(user_input):
    user_input=user_input.lower()
    if user_input in my_data.keys():
        v = my_data[user_input]
        b = "\n".join(v)
        return b
    else:
        return bii


def reply(update, context):
    user_input = update.message.text
    update.message.reply_text(do_something(user_input))


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)

def exit1(update: Update, context: CallbackContext):
    exit()
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('national_portal_of_india', npoi))
updater.dispatcher.add_handler(CommandHandler('e_health', e_health))
updater.dispatcher.add_handler(CommandHandler('National_Health_Authority', National_Health_Authority))
updater.dispatcher.add_handler(CommandHandler('HEALTHCARE_SCHEMES', HEALTHCARE_SCHEMES))
updater.dispatcher.add_handler(CommandHandler('National_institute_of_health', National_institute_of_health))
updater.dispatcher.add_handler(CommandHandler('Health_Insurance_Subsidies', Health_Insurance_Subsidies))
updater.dispatcher.add_handler(CommandHandler('exit', exit1))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.text, reply))

updater.start_polling()
