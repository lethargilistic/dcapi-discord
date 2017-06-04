import discord
from discord.ext.commands import Bot
from dcapi import Dcapi

api = Dcapi()
my_bot = Bot(command_prefix="!")

@my_bot.event
async def on_read():
    print("Client logged in")

@my_bot.command()
async def character(*args):
    if len(args) != 1:
        return await my_bot.say("Malformed args")

    search_term = args[0]

    json = api.character(search_term)
    return await my_bot.say(json)

@my_bot.command()
async def hello(*args):
    return await my_bot.say("Hello, world!")

my_bot.run("MzIxMDM4OTA5NzAwMDQ2ODQ5.DBYP6A.YX12hiJIc_vD_5o65FnqVvEwneQ")
