from random import choice

from telegram.ext import MessageHandler, Filters, run_async

import settings

RESULTS = ("Run out", "No ball", "Wide", "Bowled", "Caught", "1 run", "2 run", "3 run", "4 run", "6 run",
           "Dot ball")


def handler():
    filters = Filters.group & Filters.regex(r"^(/ball)")
    hd = MessageHandler(filters, get_result)
    return hd


@run_async
def get_result(u, c):
    member = c.bot.get_chat_member(chat_id=u.effective_chat.id, user_id=u.effective_user.id)
    if member.status not in ("administrator", "creator"):
        return
    msg_text = u.message.text
    text = "0."
    args = msg_text.split()
    if len(args) > 1 and len(args[0]) <= 5:
        text += " ".join(args[1:])
    else:
        text += msg_text
    if settings.fixed_ball:
        text += "⚾️ " + settings.fixed_ball
        settings.fixed_ball = None
    else:
        text += "⚾️ " + choice(RESULTS)
    u.message.reply_html(text, quote=True)
    return
