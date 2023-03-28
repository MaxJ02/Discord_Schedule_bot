import discord
from discord.ext import commands
from discord import File
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


BOT_TOKEN = "YOUR BOT TOKEN"
CHANNEL_ID = "DA CHANNEL ID"

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

@bot.command(name='screenshot')
async def screenshot(ctx):
    driver = webdriver.Chrome()
    driver.get("https://web.skola24.se/timetable/timetable-viewer/studiumyrgo.skola24.se/Yrgo%20L%C3%A4rdomsgatan/")
    time.sleep(2)
    input_field = driver.find_element(By.NAME, "ctl00$phMainContent$ctl00$txtId")
    input_field.clear()
    input_field.send_keys("ELA22")
    input_field.send_keys(Keys.RETURN)
    time.sleep(2)
    driver.save_screenshot('C:/Users/YOUR WINDOWS USERNAME/Desktop/screenshot.png')
    driver.quit()
    with open("screenshot.png", "rb") as f:
        picture = File(f)
        await ctx.send(file=picture)

bot.run(BOT_TOKEN)
