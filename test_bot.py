#!/usr/bin/env python3
"""
Test script for Telegram Bot functionality
Run this to test individual components without starting the full bot
"""

import asyncio
import sys
import os
from unittest.mock import Mock, AsyncMock
from datetime import datetime, timedelta

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from handlers import MessageHandlers
from config import COMMANDS, MESSAGES

class MockUpdate:
    """Mock Telegram Update object for testing"""
    
    def __init__(self, text="", chat_type="private", user_first_name="TestUser"):
        self.message = Mock()
        self.message.text = text
        self.message.chat.type = chat_type
        self.message.chat.id = 12345
        self.effective_user = Mock()
        self.effective_user.first_name = user_first_name
        self.effective_chat = Mock()
        self.effective_chat.id = 12345

class MockContext:
    """Mock Telegram Context object for testing"""
    
    def __init__(self):
        self.args = []
        self.bot = Mock()
        self.bot.username = "test_bot"
        self.job_queue = Mock()
        self.job_queue.run_once = Mock()

async def test_start_command():
    """Test the start command handler"""
    print("🧪 Testing start command...")
    
    update = MockUpdate()
    context = MockContext()
    
    try:
        await MessageHandlers.start_command(update, context)
        print("✅ Start command test passed!")
    except Exception as e:
        print(f"❌ Start command test failed: {e}")

async def test_help_command():
    """Test the help command handler"""
    print("🧪 Testing help command...")
    
    update = MockUpdate()
    context = MockContext()
    
    try:
        await MessageHandlers.help_command(update, context)
        print("✅ Help command test passed!")
    except Exception as e:
        print(f"❌ Help command test failed: {e}")

async def test_joke_command():
    """Test the joke command handler"""
    print("🧪 Testing joke command...")
    
    update = MockUpdate()
    context = MockContext()
    
    try:
        await MessageHandlers.joke_command(update, context)
        print("✅ Joke command test passed!")
    except Exception as e:
        print(f"❌ Joke command test failed: {e}")

async def test_quote_command():
    """Test the quote command handler"""
    print("🧪 Testing quote command...")
    
    update = MockUpdate()
    context = MockContext()
    
    try:
        await MessageHandlers.quote_command(update, context)
        print("✅ Quote command test passed!")
    except Exception as e:
        print(f"❌ Quote command test failed: {e}")

async def test_calculator_command():
    """Test the calculator command handler"""
    print("🧪 Testing calculator command...")
    
    update = MockUpdate()
    context = MockContext()
    
    # Test with arguments
    context.args = ["2", "+", "3"]
    
    try:
        await MessageHandlers.calculator_command(update, context)
        print("✅ Calculator command test passed!")
    except Exception as e:
        print(f"❌ Calculator command test failed: {e}")

async def test_reminder_command():
    """Test the reminder command handler"""
    print("🧪 Testing reminder command...")
    
    update = MockUpdate()
    context = MockContext()
    
    # Test with arguments
    context.args = ["30m", "Test reminder"]
    
    try:
        await MessageHandlers.reminder_command(update, context)
        print("✅ Reminder command test passed!")
    except Exception as e:
        print(f"❌ Reminder command test failed: {e}")

async def test_about_command():
    """Test the about command handler"""
    print("🧪 Testing about command...")
    
    update = MockUpdate()
    context = MockContext()
    
    try:
        await MessageHandlers.about_command(update, context)
        print("✅ About command test passed!")
    except Exception as e:
        print(f"❌ About command test failed: {e}")

async def test_settings_command():
    """Test the settings command handler"""
    print("🧪 Testing settings command...")
    
    update = MockUpdate()
    context = MockContext()
    
    try:
        await MessageHandlers.settings_command(update, context)
        print("✅ Settings command test passed!")
    except Exception as e:
        print(f"❌ Settings command test failed: {e}")

async def test_message_handler():
    """Test the regular message handler"""
    print("🧪 Testing message handler...")
    
    update = MockUpdate("Hello bot!")
    context = MockContext()
    
    try:
        await MessageHandlers.handle_message(update, context)
        print("✅ Message handler test passed!")
    except Exception as e:
        print(f"❌ Message handler test failed: {e}")

def test_config():
    """Test configuration loading"""
    print("🧪 Testing configuration...")
    
    try:
        # Test if config can be imported
        from config import COMMANDS, MESSAGES, BOT_TOKEN
        
        print(f"✅ Configuration loaded successfully!")
        print(f"   - Commands: {len(COMMANDS)} available")
        print(f"   - Messages: {len(MESSAGES)} languages")
        print(f"   - Bot token: {'Set' if BOT_TOKEN else 'Not set'}")
        
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")

def test_requirements():
    """Test if required packages can be imported"""
    print("🧪 Testing package imports...")
    
    required_packages = [
        'telegram',
        'requests',
        'asyncio',
        'logging'
    ]
    
    failed_imports = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} imported successfully")
        except ImportError:
            print(f"❌ {package} import failed")
            failed_imports.append(package)
    
    if failed_imports:
        print(f"\n⚠️  Failed imports: {', '.join(failed_imports)}")
        print("   Run: pip install -r requirements.txt")
    else:
        print("\n✅ All required packages imported successfully!")

async def run_all_tests():
    """Run all tests"""
    print("🚀 Starting Telegram Bot Tests...\n")
    
    # Test configuration and packages first
    test_config()
    print()
    test_requirements()
    print()
    
    # Test handlers
    await test_start_command()
    await test_help_command()
    await test_joke_command()
    await test_quote_command()
    await test_calculator_command()
    await test_reminder_command()
    await test_about_command()
    await test_settings_command()
    await test_message_handler()
    
    print("\n🎉 All tests completed!")
    print("\n📝 Next steps:")
    print("1. Set up your bot with @BotFather")
    print("2. Create a .env file with your BOT_TOKEN")
    print("3. Run: python bot.py")

if __name__ == "__main__":
    # Run the tests
    asyncio.run(run_all_tests())
