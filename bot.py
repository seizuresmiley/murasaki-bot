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
    '''repeats after you'''
    await bot.say(text)

@bot.command()
async def dere(option1='player | master', option2='ID'):
    '''displays deresute stats based on arguments'''
    idlength = len(option2)
    if idlength > 9 or idlength < 9 or option2.isdigit() == 'False' :
        await bot.say("Please supply valid arguments")
        return
    if option1 == 'player':

        url = ('https://deresute.me/%s/json' % option2)
        r = requests.get(url)
        dereplayerdata = r.json()
        master = dereplayerdata['cleared']['master']
        masterfc = dereplayerdata['full_combo']['master']
        playername = dereplayerdata['name']

        await bot.say('https://deresute.me/%s/large' % option2)
    elif option1 == 'master':
        #if option2.isdigit() == 'False' :
            #return
            url = ('https://deresute.me/%s/json' % option2)
            r = requests.get(url)
            dereplayerdata = r.json()
            master = dereplayerdata['cleared']['master']
            masterfc = dereplayerdata['full_combo']['master']
            playername = dereplayerdata['name']
            await bot.say("%s has %s Master clears and %s Full Combos" % (playername, master, masterfc))
    else:
        await bot.say("Please supply valid arguments")

@bot.command()
async def mltd(option1='ver | event', option2=' current / date | name / type'):
    '''displays data related to mirishita'''
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
            await bot.say("Current / last version is %s." % (mlverdata['app']['version']))
        elif option2 == 'date':
            await bot.say("Last Upated %s." % (mlverdata['app']['updateTime']))
        else:
            await bot.say("Please supply valid arguments.")
    elif option1 == 'event':
        if option2 == 'name':
            await bot.say('Current / last event name is : %s ' % (lasteventName))
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
    '''displays this bot's github link'''
    await bot.say("Check out this bot's source at https://github.com/seizuresmiley/murasaki_bot")

@bot.command()
async def despa():
    '''cito'''
    await bot.say("cito")

@bot.command()
async def bestsong():
    '''obviously the best song'''
    await bot.say("world's endo the besto https://www.youtube.com/watch?v=98rbpIzyBLg")

@bot.command()
async def nyaa(option1 = 'imas / all'):
    '''displays nyaa.si torrents. appending imas only displays Idolmaster torrents.'''
    if option1 == 'all':
        losslessurl = 'https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fnyaa.si%2F%3Fpage%3Drss%26c%3D2_1%26f%3D0'
        rl = requests.get(losslessurl)
        lsdata = rl.json()
        await bot.say(
            "Latest 3  lossless uploads on Nyaa \n \
            #1 %s \n \
            %s \n \
            #2 %s \n \
            %s \n \
            #3 %s \n \
            %s \n" \
            % (lsdata['items'][0]['title'],lsdata['items'][0]['link'],\
            lsdata['items'][1]['title'],lsdata['items'][1]['link'],\
            lsdata['items'][2]['title'],lsdata['items'][2]['link']))
    elif option1=='imas':
        imasurl = 'https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fnyaa.si%2F%3Fpage%3Drss%26q%3Didolm%2540ster%26c%3D2_1%26f%3D0'
        rl = requests.get(imasurl)
        lsdata = rl.json()
        await bot.say(
            "Latest 3 IDOLM@STER lossless uploads on Nyaa \n \
            #1 %s \n \
            %s \n \
            #2 %s \n \
            %s \n \
            #3 %s \n \
            %s \n" \
            % (lsdata['items'][0]['title'],lsdata['items'][0]['link'],\
            lsdata['items'][1]['title'],lsdata['items'][1]['link'],\
            lsdata['items'][2]['title'],lsdata['items'][2]['link']))
    else:
        return

config.read("config.ini")
token = config.get("config","token")
bot.run(token)
