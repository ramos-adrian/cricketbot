import logging
import os

import telegram.bot
from telegram import ParseMode
from telegram.ext import messagequeue as mq, Defaults

import settings
from updates import ball, toss, setball, settoss


def add_events():
    dsp = upd.dispatcher
    dsp.add_handler(ball.handler())
    dsp.add_handler(toss.handler())
    dsp.add_handler(setball.handler())
    dsp.add_handler(settoss.handler())
    return


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
token = os.environ.get('TOKEN')
settings.owners = os.environ.get('OWNER_ID').split(",")
defaults = Defaults(parse_mode=ParseMode.HTML)
upd = telegram.ext.updater.Updater(token=token, use_context=True, defaults=defaults)
add_events()

mode = os.getenv('MODE', 'polling')

if mode == "polling":
    upd.start_polling()
    print("Starting polling...")
elif mode == "heroku":
    APP_NAME = os.environ.get("APP_NAME")
    if APP_NAME:
        PORT = int(os.environ.get('PORT', '8443'))
        upd.start_webhook(listen="0.0.0.0", port=PORT, url_path=token)
        upd.bot.set_webhook("https://" + APP_NAME + ".herokuapp.com/" + token)
        upd.idle()
    else:
        print("Enviroment variable APP_NAME not defined")
else:
    print("Enviroment variable MODE not defined.")
