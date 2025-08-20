import logging
import re
import requests
import random
from datetime import datetime, timedelta
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from config import COMMANDS, MESSAGES, WEATHER_API_KEY, NEWS_API_KEY

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class MessageHandlers:
    """Handles all bot message interactions"""
    
    @staticmethod
    async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /start command"""
        user = update.effective_user
        welcome_message = f"👋 Hi {user.first_name}! {MESSAGES['en']['welcome']}"
        
        # Create inline keyboard for quick actions
        keyboard = [
            [InlineKeyboardButton("📚 Help", callback_data="help"),
             InlineKeyboardButton("🌤️ Weather", callback_data="weather")],
            [InlineKeyboardButton("📰 News", callback_data="news"),
             InlineKeyboardButton("😄 Joke", callback_data="joke")],
            [InlineKeyboardButton("💡 Quote", callback_data="quote"),
             InlineKeyboardButton("⚙️ Settings", callback_data="settings")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(welcome_message, reply_markup=reply_markup)
    
    @staticmethod
    async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /help command"""
        help_text = MESSAGES['en']['help_text']
        for command, description in COMMANDS.items():
            help_text += f"/{command} - {description}\n"
        
        help_text += "\n💡 Tip: You can also use the inline buttons for quick access!"
        
        await update.message.reply_text(help_text)
    
    @staticmethod
    async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /weather command"""
        if not WEATHER_API_KEY:
            await update.message.reply_text("Weather API key not configured.")
            return
        
        # Check if city is provided
        if context.args:
            city = ' '.join(context.args)
            await MessageHandlers._get_weather(update, city)
        else:
            await update.message.reply_text(
                "Please provide a city name.\nExample: /weather London"
            )
    
    @staticmethod
    async def news_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /news command"""
        if not NEWS_API_KEY:
            await update.message.reply_text("News API key not configured.")
            return
        
        await MessageHandlers._get_news(update)
    
    @staticmethod
    async def joke_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /joke command"""
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? He was outstanding in his field!",
            "What do you call a fake noodle? An impasta!",
            "Why did the math book look so sad? Because it had too many problems!",
            "What do you call a bear with no teeth? A gummy bear!",
            "Why don't eggs tell jokes? They'd crack each other up!",
            "What do you call a dinosaur that crashes his car? Tyrannosaurus wrecks!",
            "Why did the cookie go to the doctor? Because it was feeling crumbly!"
        ]
        
        joke = random.choice(jokes)
        await update.message.reply_text(f"😄 {joke}")
    
    @staticmethod
    async def quote_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /quote command"""
        quotes = [
            "The only way to do great work is to love what you do. - Steve Jobs",
            "Life is what happens when you're busy making other plans. - John Lennon",
            "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
            "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
            "The journey of a thousand miles begins with one step. - Lao Tzu",
            "Believe you can and you're halfway there. - Theodore Roosevelt",
            "It does not matter how slowly you go as long as you do not stop. - Confucius",
            "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt"
        ]
        
        quote = random.choice(quotes)
        await update.message.reply_text(f"💡 {quote}")
    
    @staticmethod
    async def calculator_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /calculator command"""
        if not context.args:
            await update.message.reply_text(
                "Please provide a mathematical expression.\nExample: /calculator 2 + 3 * 4"
            )
            return
        
        try:
            expression = ' '.join(context.args)
            # Basic safety check - only allow basic math operations
            if re.match(r'^[\d\s\+\-\*\/\(\)\.]+$', expression):
                result = eval(expression)
                await update.message.reply_text(f"🧮 {expression} = {result}")
            else:
                await update.message.reply_text("❌ Invalid expression. Only basic math operations are allowed.")
        except Exception as e:
            await update.message.reply_text(f"❌ Error calculating: {str(e)}")
    
    @staticmethod
    async def reminder_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /reminder command"""
        if len(context.args) < 2:
            await update.message.reply_text(
                "Please provide time and message.\nExample: /reminder 30m Buy groceries"
            )
            return
        
        try:
            time_str = context.args[0]
            message = ' '.join(context.args[1:])
            
            # Parse time (simple format: 30m, 2h, 1d)
            if time_str.endswith('m'):
                minutes = int(time_str[:-1])
                delay = timedelta(minutes=minutes)
            elif time_str.endswith('h'):
                hours = int(time_str[:-1])
                delay = timedelta(hours=hours)
            elif time_str.endswith('d'):
                days = int(time_str[:-1])
                delay = timedelta(days=days)
            else:
                await update.message.reply_text("❌ Invalid time format. Use: 30m, 2h, 1d")
                return
            
            # Schedule reminder
            context.job_queue.run_once(
                MessageHandlers._send_reminder,
                delay,
                data={'chat_id': update.effective_chat.id, 'message': message}
            )
            
            reminder_time = datetime.now() + delay
            await update.message.reply_text(
                f"⏰ Reminder set for {reminder_time.strftime('%H:%M:%S')}: {message}"
            )
            
        except ValueError:
            await update.message.reply_text("❌ Invalid time format. Use: 30m, 2h, 1d")
    
    @staticmethod
    async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /about command"""
        about_text = """
🤖 **AI Assistant Bot**

**Version:** 1.0.0
**Features:**
• Weather information
• News updates
• Jokes and quotes
• Calculator
• Reminders
• And more!

**Developer:** Created with ❤️ using python-telegram-bot
**GitHub:** Your repository link here

Use /help to see all available commands!
        """
        await update.message.reply_text(about_text, parse_mode='Markdown')
    
    @staticmethod
    async def settings_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /settings command"""
        settings_text = """
⚙️ **Bot Settings**

**Current Settings:**
• Language: English
• Notifications: Enabled
• Auto-delete: Disabled

**Available Options:**
• Change language
• Toggle notifications
• Set timezone
• Customize responses

*Settings configuration coming soon!*
        """
        await update.message.reply_text(settings_text, parse_mode='Markdown')
    
    @staticmethod
    async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle regular text messages"""
        message_type = update.message.chat.type
        text = update.message.text
        
        # Log message
        logger.info(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
        
        # Check if message is a command
        if text.startswith('/'):
            await update.message.reply_text(MESSAGES['en']['unknown_command'])
            return
        
        # Handle different types of messages
        if message_type == 'group':
            # In groups, only respond if bot is mentioned
            if '@' + context.bot.username in text:
                new_text = text.replace('@' + context.bot.username, '').strip()
                await update.message.reply_text(f"Hi! I heard: {new_text}")
        else:
            # Private chat - respond to all messages
            await update.message.reply_text(
                f"I received your message: {text}\n\nUse /help to see available commands!"
            )
    
    @staticmethod
    async def handle_callback_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle inline keyboard button presses"""
        query = update.callback_query
        await query.answer()
        
        if query.data == "help":
            await MessageHandlers.help_command(update, context)
        elif query.data == "weather":
            await query.edit_message_text("Please use /weather [city] to get weather information.")
        elif query.data == "news":
            await MessageHandlers._get_news(update, context)
        elif query.data == "joke":
            await MessageHandlers.joke_command(update, context)
        elif query.data == "quote":
            await MessageHandlers.quote_command(update, context)
        elif query.data == "settings":
            await MessageHandlers.settings_command(update, context)
    
    # Helper methods
    @staticmethod
    async def _get_weather(update: Update, city: str):
        """Get weather information for a city"""
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather"
            params = {
                'q': city,
                'appid': WEATHER_API_KEY,
                'units': 'metric'
            }
            
            response = requests.get(url, params=params)
            data = response.json()
            
            if response.status_code == 200:
                weather_info = f"""
🌤️ **Weather in {city}**
🌡️ Temperature: {data['main']['temp']}°C
💨 Wind: {data['wind']['speed']} m/s
💧 Humidity: {data['main']['humidity']}%
☁️ Description: {data['weather'][0]['description'].title()}
                """
                await update.message.reply_text(weather_info, parse_mode='Markdown')
            else:
                await update.message.reply_text(f"❌ City '{city}' not found.")
                
        except Exception as e:
            logger.error(f"Error getting weather: {e}")
            await update.message.reply_text("❌ Error getting weather information.")
    
    @staticmethod
    async def _get_news(update: Update, context: ContextTypes.DEFAULT_TYPE = None):
        """Get latest news headlines"""
        try:
            url = "https://newsapi.org/v2/top-headlines"
            params = {
                'country': 'us',
                'apiKey': NEWS_API_KEY,
                'pageSize': 5
            }
            
            response = requests.get(url, params=params)
            data = response.json()
            
            if response.status_code == 200 and data['articles']:
                news_text = "📰 **Latest News Headlines:**\n\n"
                for i, article in enumerate(data['articles'], 1):
                    title = article['title'][:100] + "..." if len(article['title']) > 100 else article['title']
                    news_text += f"{i}. {title}\n"
                
                await update.message.reply_text(news_text, parse_mode='Markdown')
            else:
                await update.message.reply_text("❌ Error getting news.")
                
        except Exception as e:
            logger.error(f"Error getting news: {e}")
            await update.message.reply_text("❌ Error getting news information.")
    
    @staticmethod
    async def _send_reminder(context: ContextTypes.DEFAULT_TYPE):
        """Send reminder message"""
        job = context.job
        await context.bot.send_message(
            chat_id=job.data['chat_id'],
            text=f"⏰ **Reminder:** {job.data['message']}"
        )
