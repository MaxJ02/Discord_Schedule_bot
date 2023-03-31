import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pyautogui
import datetime
from datetime import date 

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

BOT_TOKEN = "BOT_TOKEN_HERE" #Replace with your discord bots token. This token is private and should not be uploaded to github.
CHANNEL_ID = 1234567890      #Channel ID for the desired discord channel. Enable developer settings in discord to extract this.

date = date.today()

week_number = date.isocalendar().week +1

@bot.event
async def on_ready():
    print("Bot is alive and ready to serve")

@bot.command()
async def commands(ctx):
    await ctx.send("``` schema, commands, jagre ```")

@bot.command()
async def jagre(ctx):
    await ctx.send("Använd ditt bonnaförnuft nu!")

@bot.command()
async def test(ctx):
    await ctx.send("test")

@bot.command()
async def schema(ctx):
    channel = bot.get_channel(CHANNEL_ID)
    driver = webdriver.Chrome()
    driver.get('https://web.skola24.se/timetable/timetable-viewer/studiumyrgo.skola24.se/Yrgo%20L%C3%A4rdomsgatan/') 
    driver.set_window_size(1024, 768)
    time.sleep(3)
    pyautogui.moveTo(1000, 440, duration = 1)
    pyautogui.click(1000, 440)                
    pyautogui.typewrite("ELA22")               # Update with actual class ID (Ie ELA22, EI21 etc)  
    pyautogui.typewrite(["enter"])
    time.sleep(3)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") 
    time.sleep(2)
    await ctx.send(f"Schema vecka {week_number}")
    driver.save_screenshot('screenshot.png')
    await channel.send(file=discord.File('screenshot.png'))
    driver.quit()

bot.run(BOT_TOKEN)
