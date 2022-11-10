import telegram.ext
import pandas_datareader as web

#Opening my token text file i.e(token.txt) and reading API key
with open('token.txt', 'r') as f:
    Token = f.read()

#upon user clicking start button in telegram
def start(update, context):
    update.message.reply_text("Hello! Welcone to YATRON Bot service")

#Command handler
# help command
def help(update, context):
    update.message.reply_text("""/nThe following commands are available: 
    /start -> Welcome message
    /help -> This message
    /content -> Information about YATRON Services
    /contact -> Information about Owner
    """)

#displayes the bots purpose
def content(update, context):
    update.message.reply_text("we have videos and books!")

#Personally contacting the bot's owner
def contact(update, context):
    update.message.reply_text("You can contact me by mail")

#message handler
def handle_messgae(update, context):
    update.message.reply_text("You said {update.message.text}")

'''
Stock price lister
example - /stock AMZN
you can download any one of the listed libraries 
#pip install pandas-datareader
#pip install yfinance
'''

def stock(update, context):
    ticker = context.args[0]
    data = web.DataReader(ticker, 'yahoo')
    price = data.iloc[-1]['close']
    update.message.reply_text(f"The current price of {ticker} is {price: .2f}$!")

updater = telegram.ext.Updater(Token, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.commandHandler("start", start))
disp.add_handler(telegram.ext.commandHandler("Help", help))
disp.add_handler(telegram.ext.commandHandler("content", content))
disp.add_handler(telegram.ext.commandHandler("contact", contact))
disp.add_handler(telegram.ext.commandHandler("stock", stock))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.filters.text, handle_messgae))

updater.start_polling()
updater.idle()