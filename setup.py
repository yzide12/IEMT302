#!/usr/bin/env python3
"""
Setup script for Telegram Bot
Helps with initial configuration and setup
"""

import os
import sys
import subprocess
import shutil

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required!")
        print(f"   Current version: {sys.version}")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install requirements: {e}")
        return False

def create_env_file():
    """Create .env file from template"""
    if os.path.exists('.env'):
        print("✅ .env file already exists")
        return True
    
    if os.path.exists('env_example.txt'):
        try:
            shutil.copy('env_example.txt', '.env')
            print("✅ .env file created from template")
            print("⚠️  Please edit .env file with your bot token!")
            return True
        except Exception as e:
            print(f"❌ Failed to create .env file: {e}")
            return False
    else:
        print("❌ env_example.txt not found")
        return False

def check_env_file():
    """Check if .env file is properly configured"""
    if not os.path.exists('.env'):
        print("❌ .env file not found")
        return False
    
    try:
        with open('.env', 'r') as f:
            content = f.read()
            if 'your_telegram_bot_token_here' in content:
                print("⚠️  .env file needs to be configured with your bot token")
                return False
            if 'BOT_TOKEN=' in content:
                print("✅ .env file appears to be configured")
                return True
    except Exception as e:
        print(f"❌ Error reading .env file: {e}")
        return False
    
    return False

def run_tests():
    """Run the test suite"""
    print("🧪 Running tests...")
    try:
        subprocess.check_call([sys.executable, "test_bot.py"])
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Tests failed: {e}")
        return False

def print_next_steps():
    """Print next steps for the user"""
    print("\n" + "="*50)
    print("🚀 SETUP COMPLETE! Next steps:")
    print("="*50)
    print("1. 📱 Create your Telegram bot:")
    print("   - Open Telegram and search for @BotFather")
    print("   - Send /newbot command")
    print("   - Follow instructions to create bot")
    print("   - Copy the bot token provided")
    print()
    print("2. ⚙️  Configure your bot:")
    print("   - Edit the .env file")
    print("   - Replace 'your_telegram_bot_token_here' with your actual token")
    print("   - Save the file")
    print()
    print("3. 🚀 Start your bot:")
    print("   - Run: python bot.py")
    print("   - Your bot will start and be ready to use!")
    print()
    print("4. 📚 Test your bot:")
    print("   - Find your bot on Telegram")
    print("   - Send /start command")
    print("   - Try other commands like /help, /joke, etc.")
    print()
    print("5. 🌟 Optional enhancements:")
    print("   - Get weather API key from OpenWeatherMap")
    print("   - Get news API key from NewsAPI")
    print("   - Add these to your .env file for enhanced features")
    print("="*50)

def main():
    """Main setup function"""
    print("🤖 Telegram Bot Setup")
    print("="*30)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install requirements
    if not install_requirements():
        print("❌ Setup failed at requirements installation")
        sys.exit(1)
    
    # Create .env file
    if not create_env_file():
        print("❌ Setup failed at .env file creation")
        sys.exit(1)
    
    # Check if .env is configured
    if not check_env_file():
        print("⚠️  .env file needs manual configuration")
    
    # Run tests
    print("\n🧪 Testing bot functionality...")
    if run_tests():
        print("✅ All tests passed!")
    else:
        print("⚠️  Some tests failed, but setup can continue")
    
    # Print next steps
    print_next_steps()

if __name__ == "__main__":
    main()
