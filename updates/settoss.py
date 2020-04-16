from telegram.ext import Filters, CommandHandler

import settings

VALID_RESULTS = {"heads": "Heads", "tails": "Tails", "h": "Heads", "t": "Tails"}
usage_settoss = "Incorrect use. To use the command /settoss &lt;Toss&gt\n\nPossible types: <code>heads</code>, " \
                "<code>h</code>, <code>tails</code>, <code>t</code> "
result_set = "Next result set: <code>{result}</code>"


def handler():
    filters = Filters.private
    hd = CommandHandler("settoss", setresult, filters)
    return hd


def setresult(u, c):
    if str(u.effective_user.id) not in settings.owners:
        return
    if len(c.args) < 1:
        return u.message.reply_text(usage_settoss)
    tosstype = c.args[0].lower()
    result = VALID_RESULTS.get(tosstype)
    if result:
        settings.fixed_toss = result
        u.message.reply_text(result_set.format(result=result))
        return
    else:
        return u.message.reply_text(usage_settoss)
