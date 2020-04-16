from telegram.ext import Filters, CommandHandler

import settings

VALID_RESULTS = {"run": "Run out", "no": "No ball", "wide": "Wide", "bowled": "Bowled", "caught": "Caught",
                 "1": "1 run", "2": "2 run", "3": "3 run", "4": "4 run", "6": "6 run", "dot": "Dot ball"}
usage_setball = "Incorrect use. To use the command /setball &lt;ball type&gt\n\nPossible types: <code>run out</code>, " \
                "<code>no ball</code>, <code>wide</code>, <code>bowled</code>, <code>caught</code>, <code>dot " \
                "ball</code>, <code>1 ball</code>, <code>2 ball</code>, <code>3 ball</code>, <code>4 ball</code>, " \
                "<code>6 ball</code> "
result_set = "Next result set: <code>{result}</code>"


def handler():
    filters = Filters.private
    hd = CommandHandler("setball", setresult, filters)
    return hd


def setresult(u, c, _):
    if str(u.effective_user.id) not in settings.owners:
        return
    if len(c.args) < 1:
        return _.reply(_.l("usage_setball"))
    balltype = c.args[0].lower()
    result = VALID_RESULTS.get(balltype)
    if result:
        settings.fixed_ball = result
        _.reply(_.l("result_set", result=result))
        return
    else:
        return _.reply(_.l("usage_setball"))
