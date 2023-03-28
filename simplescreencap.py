import discord
import os
from selenium import webdriver

# Define the intents your bot will use
intents = discord.Intents.default()

# If you need to enable any additional intents, uncomment the lines below and set them to True
# intents.members = True
# intents.guilds = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Bot is ready')
    channel = client.get_channel(' YOUR CHCANNEL ID ')
    driver = webdriver.Chrome()
    driver.get('https://www.google.com')
    driver.save_screenshot('screenshot.png')
    await channel.send(file=discord.File('screenshot.png'))
    driver.quit()


client.run(' YOUR BOT TOKEN ')

