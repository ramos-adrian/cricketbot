from random import choice

from telegram.ext import CommandHandler, Filters, run_async

import settings

RESULTS = ("Heads", "Tails")


def handler():
    hd = CommandHandler("toss", toss, Filters.group)
    return hd


@run_async
def toss(u, c):
    if len(c.args) > 0:
        return
    member = c.bot.get_chat_member(chat_id=u.effective_chat.id, user_id=u.effective_user.id)
    if member.status not in ("administrator", "creator"):
        return
    if settings.fixed_toss:
        text = settings.fixed_toss
        settings.fixed_toss = None
    else:
        text = choice(RESULTS)
    u.message.reply_text(text, quote=True)
    return
