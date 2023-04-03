import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pyautogui
import datetime
from datetime import date

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

BOT_TOKEN = ""

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
async def schema(ctx, classid="ELA22"):
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

@bot.command()
async def commands(ctx):
    await ctx.send("``` schema, commands, pihl, jagre, hampus, polski, polskaharrypotter ```")

@bot.command()
async def jagre(ctx):
    await ctx.send("Använd ditt bonnaförnuft nu!")

@bot.command()
async def pihl(ctx):
    await ctx.send("so anyway, here's wonderwall: https://youtu.be/FVdjZYfDuLE")

@bot.command()
async def hampus(ctx):
    await ctx.send("git gud")

@bot.command()
async def polski(ctx):
    await ctx.send("https://img.ifunny.co/videos/4e8e61a2e0287424f8ddedf42d3d3720227e98bc7e6d4cae3fc2588a4a803ab2_1.mp4")    

@bot.command()
async def polskaharrypotter(ctx):
    await ctx.send("https://youtu.be/1puKg2thrtA")

bot.run(BOT_TOKEN)
