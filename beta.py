from discord.ext import commands
import discord
import time


BOT_TOKEN = "PLACE_BOT_TOKEN_HERE"
CHANNEL_ID = "Channel Id Here"

bot = commands.Bot(command_prefix = "{", intents = discord.Intents.all())



# On start
@bot.event
async def on_ready():
    print("I´m Awake.")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hi hi")
    while True:
        await reminder()

# Lists all active commands
@bot.command()
async def commands(ctx):
    await ctx.send("``` hello\n add\n seconds\n guess```")

# Command that allows users to add two numbers
@bot.command()
async def add(ctx, x, y):
    if x == '9' and y == '10':
        await ctx.send(f"{x} + {y} = 21 :3")
    elif not x.isdigit() or not y.isdigit():
        await ctx.send(f" u stoopid?")
    else:
        result = int(x) + int(y)
        await ctx.send(f"{x} + {y} = {result} :3")

# Counts in seconds up to ten
@bot.command()
async def seconds(ctx, i: int):
    i = int(i)
    if i <= 10:
        for n in range(1, i+1):
            await ctx.send(f"{n}")
            time.sleep(1)
    else:
        await ctx.send("sorry i only go to 10 ")

# Number guessing game
@bot.command()
async def guess(ctx):
    random_number = random.randint(1, 10)
    await ctx.send("Pick a number between 1-10 ")
    guess = None
    while True:
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.isdigit()
        guess1 = await bot.wait_for('message', check=check)
        guess = int(guess1.content)
        if guess < random_number:
            await ctx.send("low :3")
        elif guess > random_number:
            await ctx.send("high :3")
        else:
            await ctx.send("nice :3")
            await ctx.send("again???:3 (y/n) ")
            def check2(message):
                return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() in ['y', 'n']
            msg = await bot.wait_for('message', check=check2)
            if msg.content.lower() == "y":
                random_number = random.randint(1, 10)
                await ctx.send("pick again :3 ")
                
            elif msg.content.lower() == "n":
                await ctx.send("okway")
                break
            

bot.run(BOT_TOKEN)
