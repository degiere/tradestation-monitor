from process import running
from tradestation import live

if running() and live():
    print "Feelin' fine."
else:
    print "Danger Will Robinson!"
