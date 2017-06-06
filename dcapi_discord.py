import discord
from discord.ext.commands import Bot
import dcapi
from secret import token

my_bot = Bot(command_prefix="!")

@my_bot.event
async def on_read():
    print("Client logged in")

@my_bot.command()
async def character(*args):
    search_term = ""
    for part in args:
        search_term += part + " "
    search_term = search_term.strip()

    try:
        json = dcapi.character(search_term)
    except ConnectionError as msg:
        return await my_bot.say(msg)
    return await my_bot.say(json)

my_bot.run(token)
