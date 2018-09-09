import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def ready():
    print('Logged in.')
    print('Bot Name is')
    print(bot.user.name)
    print(bot.user.id)
    print('Done')


@bot.command()
async def say(text):
    await bot.say(text)

@bot.command()
async def nyaa():
    await bot.say('Nyaa is now at https://nyaa.si/')

@bot.command()
async def dere(id):
    await bot.say('https://deresute.me/%s/large' % id)


bot.run('token')
