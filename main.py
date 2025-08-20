from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("SpaCy is a great NLP library.")
for token in doc:
    print(token.text, token.pos_, token.dep_)
TOKEN: Final = "8387610539:AAFcl5gm_4UGS7GQVQTMj_kpPlAJ89oawH4"
TOKEN_USERNAME:Final = "@yandisa_bot"

#Commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Thank you for using Telegram ChatBot.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Can I help you? Provide feedback on this chat..")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is the custom command")

#Responds
def handle_response(text: str) -> str:
    proccessed: str = text.lower()

    if 'hello' in proccessed:
        return 'Hey there!'

    if 'how are you' in proccessed:
        return 'I am fine!'

    if 'i love python' in proccessed:
        return 'Remember to subscribe!'

    return 'I do not understand...'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if TOKEN_USERNAME in text:
            next_text: str = text.replace(TOKEN_USERNAME, '').strip()
            response = handle_response(next_text)
        else:
            return
    else:
        response = handle_response(text)

    print('Bot: ' + response)
    await update.message.reply_text(response)

    async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
        print(f'Update {update} caused error {context.error}')

    if __name__ == '__main__':
        print('Starting bot...')
        app = Application.builder().token(TOKEN).build()

        #Commands
        app.add_handler(CommandHandler('start', start_command))
        app.add_handler(CommandHandler('help', help_command))
        app.add_handler(CommandHandler('custom', custom_command))

        #messages
        app.add_handler(MessageHandler(filters.TEXT, handle_message))

        #Errors
        app.add_error_handler(error)

        #Polls the bot
        print('Polling bot...')
        app.run_polling(poll_interval=3)

