import discord
from selenium import webdriver

# Set up the Discord bot client
client = discord.Client()

# Set up the Selenium web driver
options = webdriver.ChromeOptions()
options.headless = True  # Run the browser in the background without a window
driver = webdriver.Chrome(options=options)

# Define a function to take a screenshot of the website
def take_screenshot():
    driver.get("https://web.skola24.se/timetable/timetable-viewer/studiumyrgo.skola24.se/Yrgo%20L%C3%A4rdomsgatan/")
    input_element = driver.find_element_by_name("input-kod")
    input_element.send_keys("ELA22")
    input_element.submit()
    driver.save_screenshot("screenshot.png")

# Define a function to send the screenshot to a Discord channel
async def send_screenshot():
    await client.wait_until_ready()
    channel = client.get_channel(YOUR_CHANNEL_ID)  # Replace with your channel ID
    with open("screenshot.png", "rb") as f:
        file = discord.File(f)
        await channel.send(file=file)

# Set up the event listener for the Discord bot
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

# Define a command to take and send a screenshot
@client.command()
async def screenshot(ctx):
    take_screenshot()
    await send_screenshot()

# Run the bot
client.run("YOUR_BOT_TOKEN")  # Replace with your bot token
