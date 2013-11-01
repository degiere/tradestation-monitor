"""
Screen scrape the desktop client to find the order bar text indicating trading server connection status
"""

from pywinauto import application, WindowNotFoundError


def connect():
    match = ".*TradeStation.*Version.*"
    app = application.Application()
    try:
        return app.connect_(title_re=match)
    except WindowNotFoundError:
        pass
    return app.connect_(title_re=match)


# From order bar:
# <Disconnected> You are disconnected from the trade server. - offline
# <Connected> SIMULATED ACCT: Connected to trade server - simulator
# <Connected> LIVE:  Connected to trade server - live
# TODO: hack! wasn't immediately obvious: better way to get this window or text directly?
def live():
    app = connect()
    wins = app.Windows_()
    for win in wins:
        text = ''.join(win.Texts())
        if "LIVE" in text:
            return True
    return False
