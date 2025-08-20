import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot Configuration
BOT_TOKEN = os.getenv('BOT_TOKEN')
BOT_USERNAME = os.getenv('BOT_USERNAME', 'YourBotUsername')

# Database Configuration (if needed)
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///bot_database.db')

# API Configuration
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

# Bot Settings
MAX_MESSAGE_LENGTH = 4096
SUPPORTED_LANGUAGES = ['en', 'es', 'fr', 'de']
DEFAULT_LANGUAGE = 'en'

# Command descriptions
COMMANDS = {
    'start': 'Start the bot and get welcome message',
    'help': 'Show available commands and their descriptions',
    'weather': 'Get current weather for a city',
    'news': 'Get latest news headlines',
    'joke': 'Get a random joke',
    'quote': 'Get an inspirational quote',
    'calculator': 'Simple calculator functionality',
    'reminder': 'Set a reminder for later',
    'about': 'Information about the bot',
    'settings': 'Configure bot preferences'
}

# Response messages
MESSAGES = {
    'en': {
        'welcome': 'Welcome! I\'m your AI assistant. How can I help you today?',
        'help_text': 'Here are the available commands:\n\n',
        'unknown_command': 'Sorry, I don\'t understand that command. Type /help for available commands.',
        'error_occurred': 'An error occurred. Please try again later.',
        'feature_not_available': 'This feature is not available yet.',
        'input_required': 'Please provide the required input.',
        'success': 'Operation completed successfully!'
    }
}
