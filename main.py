import os
import json
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler

# API key obtained from the BotFather
TOKEN = ""

# OpenWeatherMap API key
WEATHER_API_KEY = ""

def start(update: Update, context):
    """Handle the '/start' command"""
    update.message.reply_text("Hello! I am a weather bot. Send me a location to get the weather forecast.")

def weather(update: Update, context):
    """Handle the '/weather' command"""
    location = " ".join(context.args)
    if not location:
        update.message.reply_text("Please provide a location.")
        return

    # Fetch weather data from OpenWeatherMap API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHER_API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Extract weather information from the API response
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]

    # Send the weather information to the user
    update.message.reply_text(f"The weather in {location} is {description} with a temperature of {temp}°C")

def main():
    # Create the Updater and pass it the API key
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("weather", weather))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
