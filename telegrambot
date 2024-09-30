from telegram.update import Update
from telegram.ext.updater import Updater
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
# import pyttsx3
import requests
#import json
import datetime
import randfacts
import wikipedia as wiki


# engine=pyttsx3.init()
# voices=engine.getProperty('voices')
# engine.setProperty('voice',voices[1].id)
# def speak(s):
#     engine.say(s)
#     engine.runAndWait()


# url = "https://raw.githubusercontent.com/matthewreagan/WebstersEnglishDictionary/master/dictionary_compact.json"
# response = urlopen(url)
# data_json = json.loads(response.read())


#print(bot.get_me()) #A simple method for testing your bot's auth token

updater=Updater('5633741085:AAEuAbkhJ3d0UsvbVbdJlphxx4sCH5ji3n0',use_context=True)
#dispatcher=updater.dispatcher

user_api='d91a74f331bbb8b424b920304262c616'

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello sir, Welcome to the Bot.Please write\
         /help /youtube \
            /instagram /codechef\
                /greeksforgreeks /tutorialpoint \
                    /linkedin /facebook /latestnews /weather /facts to see the commands available.")
    
    

#     speak('hello sir welcome to the bot created by my boss')
#     speak('my boss is vinay')


def youtube(update: Update, context: CallbackContext):
    update.message.reply_text("youtube_url: https://www.youtube.com/")
    
    
def instagram(update: Update, context: CallbackContext):
    update.message.reply_text("Instagram_url: https://www.instagram.com/")
    
    
def codechef(update: Update, context: CallbackContext):
    update.message.reply_text("codechef_url: https://www.codechef.com/")
    
    
def greeksforgreeks(update: Update, context: CallbackContext):
    update.message.reply_text("greekforgreeks_url: https://www.greekforgreeks.com/")
    
    
def tutorialpoint(update: Update, context: CallbackContext):
    update.message.reply_text("tutorialpoint_url: https://www.tutorialpoint.com/")
    
    
def linkedin(update: Update, context: CallbackContext):
    update.message.reply_text("linkedin_url: https://in.linkedin.com/")
    
    
def facebook(update: Update, context: CallbackContext):
    update.message.reply_text("facebook_url: https://www.facebook.com/")
    
    
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)

def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)
    
    
def latestnews(update: Update, context: CallbackContext):
    news_api='7718679db5914d5b97d0903dddc201ea'
    com_api_link="https://newsapi.org/v2/top-headlines?country=in&At&apiKey="+news_api
    api_link=requests.get(com_api_link)
    api_data=api_link.json()
    arr=[]
    try:
        for i in range(10):
            arr.append(str(i+1)+". "+api_data["articles"][i]["title"]+".")
        for i in arr:
            update.message.reply_text(i)
    except Exception as e:
        update.message.reply_text(e)
 

# def weather(update: Update, context: CallbackContext):
#     user_api='d91a74f331bbb8b424b920304262c616'
#     update.message.reply_text('Enter the valid location')
#     location=
#     complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
#     api_link=requests.get(complete_api_link)
#     api_data=api_link.json()
#     if api_data['cod']=='404':
#         update.message.reply_text("Invalid city: {}, Please check the city name".format(location))
#     else:
#         temp_city=((api_data['main']['temp'])-273.15)
#         weather_desc=api_data['weather'][0]['description']
#         hmdt=api_data['main']['humidity']
#         wind_spd=api_data['wind']['speed']
#         date_time=datetime.datetime.now().strftime("%d %b %y | %H:%M:%S")
#         update.message.reply_text("weather stats for - {} || {}".format(location.upper(),date_time))
#         update.message.reply_text("current temperature is: {:.2f} deg C".format(temp_city))
#         update.message.reply_text("current weather desc :",weather_desc)
#         update.message.reply_text("current wind speed is :",wind_spd,'kmph')
#         update.message.reply_text("current humidity is :",hmdt,"%")

def facts(update: Update, context: CallbackContext):
    for i in range(10):
        x=randfacts.get_fact()
        update.message.reply_text(x)
        
def do_something(user_input):
    location=user_input.upper()
    complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+user_input+"&appid="+user_api
    api_link=requests.get(complete_api_link)
    api_data=api_link.json()
    if api_data['cod']=='404':
        update.message.reply_text("Invalid city: {}, Please check the city name".format(location))
    else:
        temp_city=((api_data['main']['temp'])-273.15)
        weather_desc=api_data['weather'][0]['description']
        hmdt=api_data['main']['humidity']
        wind_spd=api_data['wind']['speed']
        date_time=datetime.datetime.now().strftime("%d %b %y | %H:%M:%S")
        raw_str = f"weather stats for {location} || {date_time} \ncurrent temperature is: {temp_city:.2f} deg C \ncurrent weather desc : {weather_desc} \ncurrent wind speed is :{wind_spd} kmph"
    # update.message.reply_text("weather stats for - {} || {}".format(user_input.upper(),date_time))
    # update.message.reply_text("current temperature is: {:.2f} deg C".format(temp_city))
    # update.message.reply_text("current weather desc :",weather_desc)
    # update.message.reply_text("current wind speed is :",wind_spd,'kmph')
    # ("current humidity is :",hmdt,"%")
    return raw_str

def reply(update, context):
    user_input = update.message.text
    update.message.reply_text(do_something(user_input))

        
# def get_wiki(word):
#     try:
#         return wiki.summary(word)
#     except:
#         return "Not Found"

# def textpro(bot, update):
#     msg= update.message.text.lower()
#     senderName= update.message.from_user.first_name
#     chatid= update.message.chat.id
#     print("{}: {}".format(senderName, msg))
#     if(msg.startswith('wiki')):
#         bot.send_message(chat_id= chatid,text= get_wiki(msg[5:]))
#         print("Bot: Wikipedia summery of {}".format(msg[5:]))
#     else:
#         bot.send_message(chat_id= chatid, text= "{}, Invalid command".format(senderName))
#         print("Bot: Invalid command")

# def meaning(update: Update, context: CallbackContext):
#     inp=update.message.text
#     try:
#         update.message.reply_text(data_json[inp])
#     except Exception as D:
#         update.message.reply_text(D)
    

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(CommandHandler('youtube',youtube))
updater.dispatcher.add_handler(CommandHandler('instagram',instagram))
updater.dispatcher.add_handler(CommandHandler('facebook',facebook))
updater.dispatcher.add_handler(CommandHandler('linkedin',linkedin))
updater.dispatcher.add_handler(CommandHandler('greeksforgreeks',greeksforgreeks))
updater.dispatcher.add_handler(CommandHandler('codechef',codechef))
updater.dispatcher.add_handler(CommandHandler('tutorialpoint',tutorialpoint))
updater.dispatcher.add_handler(CommandHandler('youtube',youtube))
updater.dispatcher.add_handler(CommandHandler('latestnews',latestnews))
# updater.dispatcher.add_handler(CommandHandler('meanings',meaning))
# updater.dispatcher.add_handler(CommandHandler('weather',weather))
updater.dispatcher.add_handler(CommandHandler('facts',facts))
updater.dispatcher.add_handler(MessageHandler(Filters.text, reply))
# updater.dispatcher.add_handler(MessageHandler(Filters.text, textpro))
# updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
# updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
# updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
