#!/usr/bin/env python3
"""
Telegram AI Assistant Bot
A feature-rich chatbot with weather, news, jokes, quotes, calculator, and reminder functionality.
"""

import logging
import asyncio
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from config import BOT_TOKEN
from handlers import MessageHandlers

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class TelegramBot:
    """Main bot class that handles initialization and command registration"""
    
    def __init__(self):
        """Initialize the bot with token and handlers"""
        if not BOT_TOKEN:
            raise ValueError("BOT_TOKEN environment variable is required!")
        
        self.application = Application.builder().token(BOT_TOKEN).build()
        self._setup_handlers()
    
    def _setup_handlers(self):
        """Register all command and message handlers"""
        
        # Command handlers
        self.application.add_handler(CommandHandler("start", MessageHandlers.start_command))
        self.application.add_handler(CommandHandler("help", MessageHandlers.help_command))
        self.application.add_handler(CommandHandler("weather", MessageHandlers.weather_command))
        self.application.add_handler(CommandHandler("news", MessageHandlers.news_command))
        self.application.add_handler(CommandHandler("joke", MessageHandlers.joke_command))
        self.application.add_handler(CommandHandler("quote", MessageHandlers.quote_command))
        self.application.add_handler(CommandHandler("calculator", MessageHandlers.calculator_command))
        self.application.add_handler(CommandHandler("reminder", MessageHandlers.reminder_command))
        self.application.add_handler(CommandHandler("about", MessageHandlers.about_command))
        self.application.add_handler(CommandHandler("settings", MessageHandlers.settings_command))
        
        # Callback query handler for inline keyboard buttons
        self.application.add_handler(CallbackQueryHandler(MessageHandlers.handle_callback_query))
        
        # Message handler for regular text messages
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, MessageHandlers.handle_message))
        
        # Error handler
        self.application.add_error_handler(self._error_handler)
        
        logger.info("All handlers registered successfully!")
    
    async def _error_handler(self, update, context):
        """Handle errors that occur during bot operation"""
        logger.error(f"Exception while handling an update: {context.error}")
        
        # Try to send error message to user if possible
        try:
            if update and update.effective_message:
                await update.effective_message.reply_text(
                    "❌ An error occurred while processing your request. Please try again later."
                )
        except Exception as e:
            logger.error(f"Error sending error message: {e}")
    
    async def start(self):
        """Start the bot"""
        logger.info("Starting Telegram Bot...")
        
        # Get bot info
        bot_info = await self.application.bot.get_me()
        logger.info(f"Bot started: @{bot_info.username} ({bot_info.first_name})")
        
        # Start the bot
        await self.application.initialize()
        await self.application.start()
        await self.application.updater.start_polling()
        
        logger.info("Bot is now running! Press Ctrl+C to stop.")
        
        # Keep the bot running
        try:
            await asyncio.Event().wait()
        except KeyboardInterrupt:
            logger.info("Stopping bot...")
        finally:
            await self.stop()
    
    async def stop(self):
        """Stop the bot gracefully"""
        logger.info("Stopping bot...")
        
        try:
            await self.application.updater.stop()
            await self.application.stop()
            await self.application.shutdown()
            logger.info("Bot stopped successfully!")
        except Exception as e:
            logger.error(f"Error stopping bot: {e}")

def main():
    """Main function to run the bot"""
    try:
        bot = TelegramBot()
        asyncio.run(bot.start())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        raise

if __name__ == "__main__":
    main()
