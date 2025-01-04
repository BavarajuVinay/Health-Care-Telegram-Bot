from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import requests
from bs4 import BeautifulSoup
import json

updater = Updater('5931968675:AAFcznGhFb0NCGiQHV0BCGIocrSSxqIDTEE', use_context=True)
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}


#API_KEY = 'AIzaSyCd9DbiTmvIPYBGuRE6dg2FptoUJH6tUfA'

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello sir, Welcome to the Bot.Please write\
         /help \
         /best_hospitals")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Emergency Numbers  :-
    Police	-   100   
    Fire    -   101
    EMRI / AMBULANCE   -   108 or 102
    DISHA HELPLINE   -   181 OR 112
    /best_hospitals - To know about the best hospitals""")

def best_hospitals(update: Update, context: CallbackContext):
    update.message.reply_text("""Available hospitals :-
    /Fortis_Escorts_Heart_Institute(Delhi) - Best Cardiology Hospital in India"
    /Apollo_hospitals(chennai) - Best Pulmonology Hospital in India
    /Kokilaben_Dhirubhani_Ambani(Mumbai) - Best Neurosurgery Hospital in India
    """)

def Fortis_Escorts_Heart_Institute(update: Update, context: CallbackContext):
    update.message.reply_text("Fortis Escorts Heart Institute(Delhi): https://www.fortisescorts.in/")

def Apollo_hospitals(update: Update, context: CallbackContext):
    update.message.reply_text("Apollo_hospitals: https://www.apollohospitals.com/chennaiapolloconsultleads/?utm_source=google&utm_medium=cpc&utm_campaign=TM_Brand_Search_Chennai&utm_content=brand&gclid=Cj0KCQiA4aacBhCUARIsAI55maF3Xz_BMs5t9s8QJ82sV6-2HP8GsG2keRynYHpUTKfrPMxr9cec3N4aAo1rEALw_wcB")

def Kokilaben_Dhirubhani_Ambani(update: Update, context: CallbackContext):
    update.message.reply_text("Kokilaben_Dhirubhani_Ambani(Mumbai): https://www.kokilabenhospital.com/")


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)

def location(user_input):
     url = 'https://www.google.com/search?tbs=lf:1,lf_ui:2&tbm=lcl&sxsrf=ALiCzsYXdFritIKtlJDrF6gdq5fwv55D5A:1670002031276&q=' + "hospitals in "+ user_input
     page = requests.get(url, headers=headers)
     obj = BeautifulSoup(page.content, 'html.parser')
     res = obj.find(class_='rlfl__tls rl_tls').get_text()
     return res

def reply(update, context):
    user_input = update.message.text
    update.message.reply_text(location(user_input))


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('Fortis_Escorts_Heart_Institute', Fortis_Escorts_Heart_Institute))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('best_hospitals', best_hospitals))
updater.dispatcher.add_handler(CommandHandler('Fortis_Escorts_Heart_Institute', Fortis_Escorts_Heart_Institute))
updater.dispatcher.add_handler(CommandHandler('Apollo_hospitals', Apollo_hospitals))
updater.dispatcher.add_handler(CommandHandler('Kokilaben_Dhirubhani_Ambani', Kokilaben_Dhirubhani_Ambani))
updater.dispatcher.add_handler(MessageHandler(Filters.text, reply))
updater.start_polling()
