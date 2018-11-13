__authors__ = 'electric-blue-green'
__license__ = 'MIT'
__status__ = 'Prototype'
import discord
from discord.ext import commands
import sqlite3
import os
import subprocess
import time
import requests
import asyncio
import random

class shellcog:
    def __init__(self, bot):
        print(0)
        self.bot = bot
        word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
        response = requests.get(word_site)
        self.wordslist = response.text.splitlines()
        bot.loop.create_task(self.thanos())

    async def thanos(self):
        #print(1)
        await self.bot.wait_until_ready()
        #print(2)
        while not self.bot.is_closed():
            #print(type(wordslist))
            #print(random.choice(wordslist))
            word=(random.choice(self.wordslist))
            content=("thanos "+word+"\nthanos "+word)
            await self.bot.get_channel(499898214099582976).send(content)
            await asyncio.sleep(3600)


def setup(bot):
    bot.add_cog(shellcog(bot))
