#https://docs.python.org/3/library/os.html
import os
#https://pypi.org/project/python-dotenv/
from dotenv import load_dotenv
#https://discordpy.readthedocs.io/en/latest/
import discord

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('ping'):
        await message.channel.send('Pong!')

client.run(os.getenv('DISCORD_TOKEN'))