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
import time
import pyautogui
import datetime

# sets prefix and intents
bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

# token for the bot
BOT_TOKEN = " " 

# runs the script every sunday at 13:00 UTC (15:00 Swedish summer time)
@tasks.loop(time=datetime.time(hour=13, minute=00)) # UTC time
async def job_loop(classid="ela22"): # classid is the class id, can be changed to any class id.
    week_num = datetime.date.today().isocalendar()[1] + 1 # gets the current week number and adds 1 to it, as the schedule is for the next week.
    weekday = datetime.datetime.utcnow().weekday() # gets the current weekday
    if weekday == 6:    # if it's sunday, run the script.
        channel = bot.get_channel(1234567890) # channel id
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
    print("Bot online")
    if not job_loop.is_running():
        job_loop.start()
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)    



# Old way of fetching the week number, used in the !schema command for testing purposes.
def old_get_week_number(date): 
    
    if date.weekday() < 5:
        return date.isocalendar().week
    else:
        return date.isocalendar().week + 1

oldtoday = datetime.date.today()
week_number = old_get_week_number(oldtoday)

# command to run the script manually
@bot.command()
async def schema(ctx, classid="ela22"):
    #ctx = bot.get_channel(0123456789) can be used if only one channel is used.
    driver = webdriver.Chrome()
    driver.get('https://web.skola24.se/timetable/timetable-viewer/studiumyrgo.skola24.se/Yrgo%20L%C3%A4rdomsgatan/') #replace with your school's schedule page
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

# command to test the bot and see if it's online.
@bot.tree.command(name="pong")
async def pong(interaction: discord.Interaction):
    await interaction.response.send_message(f"ping")    

# command that posts a picture of ohms law.
@bot.command()
async def ohm(ctx):
    await ctx.send("https://vattenkraft.info/teori/bilder/ohmslag.gif")

bot.run(BOT_TOKEN)
