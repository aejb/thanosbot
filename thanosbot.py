__authors__ = 'electric-blue-green'
__license__ = 'MIT'
__status__ = 'Prototype'
import discord
from discord.ext import commands
import sqlite3
import os
import subprocess
import traceback
import sys

initial_extensions=['cog']

def gettoken():
    tokenfile = open("token.txt", "r")
    tokenstring = tokenfile.read()
    tokentoken = tokenstring.split("\n")
    token = str(tokentoken[0])
    return token
token = gettoken()

description = "use tbhelp"

#afkarray=[]


bot = commands.Bot(command_prefix=["tb"], description=description)



if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print("Failed to load" + extension, file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(token)
