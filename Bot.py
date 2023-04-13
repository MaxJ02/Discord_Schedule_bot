import discord
from discord.ext import commands
from discord import app_commands
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pyautogui
import datetime
from datetime import date

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

BOT_TOKEN = ""  #Replace with your discord bots token. This token is private and should not be uploaded to github.


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
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.command()
async def schema(ctx, classid="ELA22"): # Asks for a classid to be sent after !schema, if none is provided, the default value of ELA22 will be used.
    driver = webdriver.Chrome()
    driver.get('https://web.skola24.se/timetable/timetable-viewer/studiumyrgo.skola24.se/Yrgo%20L%C3%A4rdomsgatan/') #replace with desired skola24 url.
    driver.set_window_size(1024, 768)
    time.sleep(1)
    pyautogui.moveTo(850, 420, duration = 1) #Might need to be adjusted with trial and error.
    pyautogui.click(850, 420)                #ditto
    pyautogui.typewrite(classid)             
    pyautogui.typewrite(["enter"])
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") 
    time.sleep(1)
    await ctx.send(f"Schema vecka {week_number} för {classid}")
    driver.save_screenshot('screenshot.png')
    await ctx.send(file=discord.File('screenshot.png'))

bot.run(BOT_TOKEN)    
   
#The ones below are just fun extras.

#@bot.tree.command(name="commands")
#async def commands(interaction: discord.Interaction):
#    await interaction.response.send_message(f"schema, commands, pihl, jagre, hampus, polski, polskaharrypotter") 
#
#        
#@bot.command()
#async def commands2(ctx):
#    await ctx.send("``` schema, commands, pihl, jagre, hampus, polski, polskaharrypotter ```")
#
#@bot.command()
#async def jagre(ctx):
#    await ctx.send("Använd ditt bonnaförnuft nu!")
# 
#@bot.command()
#async def pihl(ctx):
#     await ctx.send("so anyway, here's wonderwall: https://youtu.be/FVdjZYfDuLE")
# 
#@bot.command()
#async def hampus(ctx):
#   await ctx.send("git gud")
#
#@bot.command()
#async def polski(ctx):
#    await ctx.send("https://img.ifunny.co/videos/4e8e61a2e0287424f8ddedf42d3d3720227e98bc7e6d4cae3fc2588a4a803ab2_1.mp4")    
# 
#@bot.command()
#async def polskaharrypotter(ctx):
#     await ctx.send("https://youtu.be/1puKg2thrtA")
#    
#@bot.tree.command(name="hello")
#async def hello(interaction: discord.Interaction):
#    await interaction.response.send_message(f"Tjena {interaction.user.mention}! Detta är ett slash commando!")
#    
#@bot.tree.command(name="ping")
#async def ping(interaction: discord.Interaction):
#    await interaction.response.send_message(f"pong")         
#       
#@bot.command()
#async def bill(ctx):
#    await ctx.send("Kretsen ska inte se ut så. https://ifkgoteborg.se/wp-content/uploads/2020/01/IFK-favicon.png")
#
#@bot.command()
#async def ohm(ctx):
#    await ctx.send("https://vattenkraft.info/teori/bilder/ohmslag.gif")
#
#bot.run(BOT_TOKEN)
