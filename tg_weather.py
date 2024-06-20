import telebot
from telebot import types
import requests
import json
bot=telebot.TeleBot('7458293521:AAFaODGeMjAN8ii1RfianyYNKJVewqe6u3Y')
API='31f9cc2d886bac37db957e066854fe93'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет,рад тебя видеть! Напиши название города!')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city=message.text.strip().lower()
    res=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code==200: 
        data= json.loads(res.text)
        temp=data["main"]["temp"]
        bot.reply_to(message,f'Сейчас погода: {temp} ℃')

        image='weather/sun.png' if temp > 5.0 else 'weather/sun_cold.png'
        file=open('./' + image,'rb')
        bot.send_photo(message.chat.id,file)
    else:
        bot.reply_to(message,'Город указан не верно')




bot.infinity_polling()