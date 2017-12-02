import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(message)s',
                        level = logging.INFO,
                        filename = 'bot_2.log'
                        ) 

def start_bot(bot, update):
    mytext = "Hello, {}!I'm simple bot and understand only {} command".format(update.message.chat.first_name, '/start')
    update.message.reply_text(mytext)

def chat(bot, update):
    users_text = update.message.text
    logging.info(users_text.decode("utf-8").encode("cp1251"))
    update.message.reply_text(users_text)

def main():
    updtr = Updater('500991328:AAHB3-Uoo9kfbAFptfviMvlgIV1V-iHzwl4')
    updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
    updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))
    updtr.start_polling()
    updtr.idle()

if __name__ == "__main__":
    logging.info('Bot started')
    main()
