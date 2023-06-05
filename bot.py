##############################################
# This bot is made for the ela22 Discord server
# It's purpose is to post the schedule for the
# current week in the #schema channel.
#   - It uses Selenium to open a browser and
#     take a screenshot of the schedule.
#   - It uses PyAutoGUI to type in the class
#     ID and press enter.
#   - It uses Discord.py to post the screenshot
#     in the #schema channel.
#   - It uses the schedule module to run the
#     script every sunday at 13:00 UTC.
##############################################

# includes
import discord
from discord.ext import commands, tasks
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pyautogui
import datetime
from datetime import date
import schedule

# sets prefix and intents
bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

# token for the bot
BOT_TOKEN = " "

# gets the current week number, currently doesn't work as intended for more than one week
my_date = datetime.date.today() 
year, week_num, day_of_week = my_date.isocalendar()

# runs the script every sunday at 13:00 UTC (15:00 Swedish summer time)
@tasks.loop(time=datetime.time(hour=13, minute=00)) # UTC time
async def job_loop(classid="ela22"):
    weekday = datetime.datetime.utcnow().weekday()
    if weekday == 6:    # sunday
        channel = bot.get_channel(123456789) # channel id
        driver = webdriver.Chrome()
        driver.get('https://web.skola24.se/timetable/timetable-viewer/studiumyrgo.skola24.se/Yrgo%20L%C3%A4rdomsgatan/') 
        driver.set_window_size(1024, 768) # set window size, might need to be changed depending on screen resolution
        time.sleep(3)
        pyautogui.moveTo(1000, 440, duration = 1) # moves mouse to the search bar, values might need to be changed depending on screen resolution
        pyautogui.click(1000, 440)              # clicks the search bar   
        pyautogui.typewrite(classid)             
        pyautogui.typewrite(["enter"])
        time.sleep(3)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") 
        time.sleep(2)
        await channel.send(f"Schema vecka {week_num} för {classid}")
        driver.save_screenshot('screenshot.png')
        await channel.send(file=discord.File('screenshot.png'))

# checks if the loop is running, if not it starts it
@bot.event
async def on_ready():
    if not job_loop.is_running():
        job_loop.start()

# command to run the script manually
@bot.command()
async def schema(ctx, classid="ela22"):
    #ctx = bot.get_channel(0123456789) can be used if only one channel is used.
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
    await ctx.send(f"Schema vecka {week_num} för {classid}")
    driver.save_screenshot('screenshot.png')
    await ctx.send(file=discord.File('screenshot.png'))

bot.run(BOT_TOKEN)
