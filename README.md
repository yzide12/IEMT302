# 🤖 Telegram AI Assistant Bot

A feature-rich Telegram chatbot built with Python that provides weather information, news updates, jokes, quotes, calculator functionality, and reminder services.

## ✨ Features

- **🌤️ Weather Information** - Get current weather for any city
- **📰 News Updates** - Latest news headlines from around the world
- **😄 Jokes & Quotes** - Random jokes and inspirational quotes
- **🧮 Calculator** - Simple mathematical calculations
- **⏰ Reminders** - Set timed reminders for important tasks
- **⚙️ Settings** - Customizable bot preferences
- **📱 Inline Keyboard** - Easy-to-use button interface
- **🌍 Multi-language Support** - Ready for internationalization

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Telegram account
- Internet connection

### Installation

1. **Clone or download the project files**
   ```bash
   # If you have git installed
   git clone <your-repository-url>
   cd IEMT302
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Telegram Bot**
   - Open Telegram and search for `@BotFather`
   - Send `/newbot` command
   - Follow the instructions to create your bot
   - Copy the bot token provided

4. **Configure environment variables**
   - Copy `env_example.txt` to `.env`
   - Fill in your bot token and optional API keys:
   ```bash
   BOT_TOKEN=your_actual_bot_token_here
   BOT_USERNAME=your_bot_username
   ```

5. **Run the bot**
   ```bash
   python bot.py
   ```

## 🔧 Configuration

### Required Configuration

- **BOT_TOKEN**: Your Telegram bot token from @BotFather

### Optional Configuration

- **WEATHER_API_KEY**: OpenWeatherMap API key for weather features
  - Get free API key from [OpenWeatherMap](https://openweathermap.org/api)
- **NEWS_API_KEY**: News API key for news features
  - Get free API key from [NewsAPI](https://newsapi.org/)
- **BOT_USERNAME**: Your bot's username (without @)

## 📱 Available Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/start` | Start the bot and get welcome message | `/start` |
| `/help` | Show all available commands | `/help` |
| `/weather` | Get weather for a city | `/weather London` |
| `/news` | Get latest news headlines | `/news` |
| `/joke` | Get a random joke | `/joke` |
| `/quote` | Get an inspirational quote | `/quote` |
| `/calculator` | Perform calculations | `/calculator 2 + 3 * 4` |
| `/reminder` | Set a timed reminder | `/reminder 30m Buy groceries` |
| `/about` | Bot information | `/about` |
| `/settings` | Bot settings | `/settings` |

## 🎯 Usage Examples

### Weather Information
```
/weather New York
```
Returns current weather conditions for New York.

### Calculator
```
/calculator (15 + 25) * 2
```
Performs mathematical calculations safely.

### Reminders
```
/reminder 2h Call mom
```
Sets a reminder to "Call mom" in 2 hours.

## 🏗️ Project Structure

```
IEMT302/
├── bot.py              # Main bot application
├── handlers.py         # Message and command handlers
├── config.py           # Configuration and constants
├── requirements.txt    # Python dependencies
├── env_example.txt     # Environment variables template
└── README.md          # This file
```

## 🔒 Security Features

- **Input Validation**: All user inputs are validated before processing
- **Safe Calculator**: Mathematical expressions are restricted to basic operations
- **Error Handling**: Comprehensive error handling and logging
- **Rate Limiting**: Built-in protection against spam

## 🚀 Deployment Options

### Local Development
```bash
python bot.py
```

### Production Deployment
- **Heroku**: Deploy as a web app
- **VPS**: Run on a virtual private server
- **Docker**: Containerize the application
- **Cloud Functions**: Serverless deployment

## 🧪 Testing

Test your bot by:
1. Starting the bot locally
2. Opening Telegram
3. Finding your bot by username
4. Sending `/start` command
5. Testing various features

## 🔧 Customization

### Adding New Commands
1. Add command handler in `handlers.py`
2. Register handler in `bot.py`
3. Update `config.py` with command description
4. Add to help menu

### Modifying Responses
- Edit message templates in `config.py`
- Modify handler logic in `handlers.py`
- Add new inline keyboard options

### API Integration
- Add new API keys to `config.py`
- Create new handler methods in `handlers.py`
- Update requirements.txt if needed

## 📊 Monitoring and Logging

The bot includes comprehensive logging:
- User interactions
- Command usage
- Error tracking
- Performance metrics

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter issues:
1. Check the logs for error messages
2. Verify your bot token is correct
3. Ensure all dependencies are installed
4. Check your internet connection
5. Verify API keys (if using weather/news features)

## 🔮 Future Enhancements

- [ ] Database integration for user preferences
- [ ] Multi-language support
- [ ] Advanced AI features
- [ ] Image generation capabilities
- [ ] Voice message support
- [ ] Group management features
- [ ] Analytics dashboard

---

**Happy Botting! 🤖✨**
