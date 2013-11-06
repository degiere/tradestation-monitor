TradeStation Monitor
====================
If machine is down, or TradeStation is not running, or it's not connected to the live trade server, send an alert

Design
------
* Python web server runs on startup
* A single controller checks if the client is running and connected and shows a web page with success or fail
* If machine is down, page request will timeout and alerted
* If keyword: fail shows alerted
* Otherwise if pass is shown, no alert
* Pingdom checks web page and sends sms if fail or timeout

References
----------
* Python - http://www.python.org/
* WMI (Windows Management Instrumentation) - https://pypi.python.org/pypi/WMI/
* Pywinauto - https://code.google.com/p/pywinauto/
* Flask - http://flask.pocoo.org/
* Pingom - https://www.pingdom.com/
