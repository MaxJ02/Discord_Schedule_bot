#####################################################################################
#
# clientbot.py: First version of this bot. Only works by running the script directly.
#               Unable to be summoned with any ! commands. 
#
######################################################################################

# Imports
import discord
import os
from selenium import webdriver
import time
import pyautogui

# Defines the intents the bot will use
intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Bot is ready to cook')
    channel = client.get_channel(1234567890)  #Replace with the desired discord channel ID.
    driver = webdriver.Chrome()
    driver.get('https://web.skola24.se/timetable/timetable-viewer/studiumyrgo.skola24.se/Yrgo%20L%C3%A4rdomsgatan/') #Can be replaced with the URL to your skola24 domain.
    time.sleep(5)  # wait for 5 seconds
    pyautogui.moveTo(1000, 440, duration = 1) #Actual x and y values might need to be tinkered with depending on your screens resolution.
    pyautogui.click(1000, 440)                # ^ Can be achieved through simple trial and error 
    pyautogui.typewrite("ELA22")              #Replace with desired class ID. 
    pyautogui.typewrite(["enter"])
    time.sleep(5)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") #scrolls down all the way
    time.sleep(2)                             #Waits 2 seconds
    driver.save_screenshot('screenshot.png')
    await channel.send(file=discord.File('screenshot.png'))
    driver.quit()

client.run('abcdefghijklmnopqrstuvwxyz1234567890')  #Replace wtih your discord bots private token. 
