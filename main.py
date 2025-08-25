import os
import random
import spacy
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler

#Load environment variables
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
async def state0_handler(update, context):
    """use SpaCy to handle state0"""
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(update.message.text)
    reply = ''
    # What shall we do with the doc? Put your response in reply.
    if reply:
        update.message.reply_text(reply)
    # most likely, a different state needs to be returned
    return 'STATE0'


async def start(update, context):
    """announce yourself in a way that suggests the kind of interaction expected"""
    await update.message.reply_text("Hi! I am your bot. How may I be of service?")
    # most likely, some initial state needs to be returned
    return 'STATE0'


async def cancel(update, context):
    """gracefully exit the conversation"""
    await update.message.reply_text("Thanks for the chat. I'll be off then!")
    return ConversationHandler.END


async def help(update, context):
    """what situations give rise to a request such as this?"""
    await update.message.reply_text("The help needs to go here.")
    return


def main():
    """the bot's main message loop is set up and run from here"""
    application = Application.builder().token(TOKEN).build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler(['start'], start)],
        states={
            # a dict of states needs to be inserted here
            'STATE0': [MessageHandler(filters.TEXT & ~filters.COMMAND, state0_handler)],
        },
        fallbacks=[CommandHandler(['cancel'], cancel),
                   CommandHandler('help', help)]
    )
    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == '__main__':
    main()