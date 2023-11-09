from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final='6642093811:AAHlkcNKqxE3FfMm_-M-DOWXkDsdA4axqMc'
BOT_USERNAME: Final='@MeydanHaravLondin_bot'

#COMMANDS
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('send me the text you want to chunk')

#Responses

def handle_response(text: str) -> str:
    #build here my logic
    return 'blablabla'

async def handle_massage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str=update.message.chat.type
    text: str=update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    #handle talk to bot from a group or private chat
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str=text.replace(BOT_USERNAME, '').strip()
            response: str=handle_response(new_text)
        else:
            return
    else:
        response: str=handle_response(text)
    
    print('Bot:',response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__=='__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_massage))

    # Error
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=5)
