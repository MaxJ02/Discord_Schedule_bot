import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pyautogui
import datetime
from datetime import date

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

BOT_TOKEN = "abc123def456"  #Replace with your discord bots token. This token is private and should not be uploaded to github.

# Checks the current day of the week. If its a weekday (mon - fri), the current week & schedule will be printed. Else, The next weeks number and schedule will be printed.
def get_week_number(date):
    
    if date.weekday() < 5:
        return date.isocalendar().week
    else:
        return date.isocalendar().week + 1

today = datetime.date.today()
week_number = get_week_number(today)

@bot.event
async def on_ready():
    print("Bot is alive")

@bot.command()
async def commands(ctx):
    await ctx.send("``` schema, commands, pihl, jagre ```")

@bot.command()
async def jagre(ctx):
    await ctx.send("Använd ditt bonnaförnuft nu!")

@bot.command()
async def pihl(ctx):
    await ctx.send("So anyway, here's wonderwall: https://youtu.be/FVdjZYfDuLE")

@bot.command()
async def schema(ctx, classid="ELA22"): # Asks for a classid, if none is provided, the default value of ELA22 will be used. 
    driver = webdriver.Chrome()
    driver.get('https://web.skola24.se/timetable/timetable-viewer/studiumyrgo.skola24.se/Yrgo%20L%C3%A4rdomsgatan/') 
    driver.set_window_size(1024, 768)
    time.sleep(3)
    pyautogui.moveTo(1000, 440, duration = 1)
    pyautogui.click(1000, 440)                
    pyautogui.typewrite(classid)             
    pyautogui.typewrite(["enter"])
    time.sleep(3)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") 
    time.sleep(2)
    await ctx.send(f"Schema vecka {week_number} för {classid}")
    driver.save_screenshot('screenshot.png')
    await ctx.send(file=discord.File('screenshot.png'))
    driver.quit()

bot.run(BOT_TOKEN)
