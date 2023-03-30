import discord
from discord.ext import commands
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pyautogui

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

BOT_TOKEN = ""
CHANNEL_ID =


@bot.event
async def on_ready():
    print("Bot is alive")

@bot.command()
async def commands(ctx):
    await ctx.send("``` schema```")

@bot.command()
async def schema(ctx):
    channel = bot.get_channel(CHANNEL_ID)
    driver = webdriver.Chrome()
    driver.get('https://web.skola24.se/timetable/timetable-viewer/studiumyrgo.skola24.se/Yrgo%20L%C3%A4rdomsgatan/') 
    driver.set_window_size(1024, 768)
    time.sleep(5)  # wait for 5 seconds
    pyautogui.moveTo(1000, 440, duration = 1)
    pyautogui.click(1000, 440)                
    pyautogui.typewrite("CLASS_NAME_PLACEHOLDER")         # Update with actual class ID (Ie ELA22, EI21 etc)     
    pyautogui.typewrite(["enter"])
    time.sleep(5)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") 
    time.sleep(2) 
    driver.save_screenshot('screenshot.png')
    await channel.send(file=discord.File('screenshot.png'))
    driver.quit()

bot.run(BOT_TOKEN)
