import discord
import asyncio
from discord.ext import commands
import requests
import json
import configparser

bot = commands.Bot(command_prefix='m!')
config = configparser.ConfigParser()



@bot.event
async def on_ready():
    print('Logged in.')
    print('Bot Name is')
    print(bot.user.name)
    print(bot.user.id)
    print('Done')


@bot.command()
async def say(text):
    await bot.say(text)

@bot.command()
async def dere(option1, option2):
    option1 == null
    option2 == null

    url = ('https://deresute.me/%s/json' % option2)
    r = requests.get(url)
    dereplayerdata = r.json()
    master = dereplayerdata['cleared']['master']
    masterfc = dereplayerdata['full_combo']['master']
    if option1 == 'player':
        await bot.say('https://deresute.me/%s/large' % option2)
    elif option1 == 'master':
        await bot.say("This Producer has %s Master clears and %s Full Combos" % (master, masterfc))
    else:
        await bot.say("Please supply valid arguments")

@bot.command()
async def mltd(option1, option2):
    option1 == null
    option2 == null

    url = 'https://api.matsurihi.me/mltd/v1/version/latest'
    r = requests.get(url)
    mlverdata = r.json()
    re = requests.get('https://api.matsurihi.me/mltd/v1/events')
    #somehow mleventdata is a list and not a dict
    mleventdata = re.json()
    lasteventinfo = mleventdata[-1]
    lasteventID = lasteventinfo['id']
    lasteventName = lasteventinfo['name']
    lasteventType = int(lasteventinfo['type'])

    #Event Types include:
    #1 : Theater Show Time
    #2 : Millicolle
    #3 : Platinum Star Theater (Token)
    #4 : Platinum Star Theater (Gauge)
    #5 : Anniversary
    if option1 == 'ver':
        if option2 == 'current':
            await bot.say("Current version is %s." % (mlverdata['app']['version']))
        elif option2 == 'date':
            await bot.say("Last Upated %s." % (mlverdata['app']['updateTime']))
        else:
            await bot.say("Please supply valid arguments.")
    elif option1 == 'event':
        if option2 == 'name':
            await bot.say('Event Name is : %s ' % (lasteventName))
        elif option2 == 'type':
            if lasteventType == 1:
                await bot.say("Event type is : Theater Show Time.")
            elif lasteventType == 2:
                await bot.say("Event Type is : Millicolle.")
            elif lasteventType == 3:
                await bot.say("Event Type is : Platinum Star Theater (Tokens)")
            elif lasteventType == 4:
                await bot.say("Event Type is : Platinum Star Theater (Gauge)")
            elif lasteventType == 5:
                await bot.say("Event Type is : Anniversary Event")
            else:
                await bot.say("Event ID invalid. Please contact bot owner to update.")
    else:
        await bot.say("Please supply valid arguments")

@bot.command()
async def github():
    await bot.say("Check out this bot's source at https://github.com/seizuresmiley/murasaki_bot")


config.read("config.ini")
token = config.get("config","token")
bot.run(token)
