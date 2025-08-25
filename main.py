#!/usr/bin/env python3
import os
import spacy
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler

# Load environment variables
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Load SpaCy model once (not inside handler)
nlp = spacy.load("en_core_web_sm")

# Define states
STATE0 = 0


async def state0_handler(update, context):
    """use SpaCy to handle state0"""
    text = update.message.text
    doc = nlp(text)

    # Example: echo back nouns from the message
    nouns = [token.text for token in doc if token.pos_ == "NOUN"]
    reply = f"I found these nouns: {', '.join(nouns)}" if nouns else "I didn’t find any nouns."

    await update.message.reply_text(reply)
    return STATE0


async def start(update, context):
    """announce yourself in a way that suggests the kind of interaction expected"""
    await update.message.reply_text("Hi! I am your bot. How may I be of service?")
    return STATE0


async def cancel(update, context):
    """gracefully exit the conversation"""
    await update.message.reply_text("Thanks for the chat. I'll be off then!")
    return ConversationHandler.END


async def help(update, context):
    """what situations give rise to a request such as this?"""
    await update.message.reply_text("Send me a message, and I’ll try to analyze it with NLP!")
    return


def main():
    """the bot's main message loop is set up and run from here"""
    application = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            STATE0: [MessageHandler(filters.TEXT & ~filters.COMMAND, state0_handler)],
        },
        fallbacks=[CommandHandler("cancel", cancel),
                   CommandHandler("help", help)]
    )

    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == "__main__":
    main()
