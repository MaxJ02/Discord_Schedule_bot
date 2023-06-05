import discord
from discord.ext import commands, tasks
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pyautogui
import datetime
from datetime import date
import schedule

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

BOT_TOKEN = " "

my_date = datetime.date.today() 
year, week_num, day_of_week = my_date.isocalendar()

@tasks.loop(time=datetime.time(hour=13, minute=00)) # UTC time
async def job_loop(classid="ela22"):
    weekday = datetime.datetime.utcnow().weekday()
    if weekday == 6:    # sunday
        channel = bot.get_channel(1234567890) 
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
        await channel.send(f"Schema vecka {week_num} för {classid}")
        driver.save_screenshot('screenshot.png')
        await channel.send(file=discord.File('screenshot.png'))


@bot.event
async def on_ready():
    if not job_loop.is_running():
        job_loop.start()

@bot.command()
async def schema(ctx, classid="ela22"):
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
