import discord
import os
from selenium import webdriver
import time

# Define the intents your bot will use
intents = discord.Intents.default()

# If you need to enable any additional intents, uncomment the lines below and set them to True
# intents.members = True
# intents.guilds = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Bot is ready')
    channel = client.get_channel(1234567890) #replace with actual channel id, currently ignores this and sends the screencap to general anyway, but its still required.
    driver = webdriver.Chrome()
    driver.get('https://web.skola24.se/timetable/timetable-viewer/studiumyrgo.skola24.se/Yrgo%20L%C3%A4rdomsgatan/')
    time.sleep(5)  # wait for 5 seconds
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2) #waits for another 2 seconds to make sure the scrolling is successfull.
    driver.save_screenshot('screenshot.png')
    await channel.send(file=discord.File('screenshot.png'))
    driver.quit()

client.run('BOT TOKEN')



#upcoming:
#Enter the class ID in the correct field.
#Add a weekly timer.
#Send in the correct channel.
