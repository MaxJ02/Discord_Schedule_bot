from discord.ext import commands
import discord
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


BOT_TOKEN = "PLACE_BOT_TOKEN_HERE"
CHANNEL_ID = 123456789            # Replace with actual channel ID
WEBSITE_URL = "https://web.skola24.se/timetable/timetable-viewer/studiumyrgo.skola24.se/Yrgo%20L%C3%A4rdomsgatan/"

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no window pops up)
chrome_options.add_argument("--no-sandbox")  # Disable sandbox mode (may be necessary on some systems)
chrome_driver_path = "./chromedriver"  # Path to the chromedriver executable (Can be changed to firefox if the two above commands are changed as well.

def take_screenshot(url, search_text):
    driver = webdriver.Chrome(chrome_driver_path, options=chrome_options)
    driver.get(url)
    search_field = driver.find_element_by_name("Ange ID")
    search_field.clear()
    search_field.send_keys(search_text)
    search_field.submit()
    time.sleep(5) # Wait for the page to load
    screenshot_path = os.path.abspath("screenshot.png")
    driver.save_screenshot(screenshot_path)
    driver.quit()
    return screenshot_path

bot = commands.Bot(command_prefix = "...", intents = discord.Intents.all())

@bot.command()
async def screenshot(ctx):
    try:
        screenshot_path = take_screenshot(WEBSITE_URL, "ELA22")
        with open(screenshot_path, "rb") as file:
            screenshot = discord.File(file)
        await ctx.send(file=screenshot)
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

bot.run(BOT_TOKEN)
