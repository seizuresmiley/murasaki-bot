# Murasaki Bot

![Echizen Murasaki](https://i.imgur.com/m3Pco1h.jpg)


A very basic Discord bot made to aid me in studying Python.

Despite it being named after a Tokyo 7th Sisters character, most of the features are things that deal with Idolmaster mobile games.

Data is pulled from these sources:

https://www.matsurihi.me/

https://deresute.me/


## Dependencies

This bot uses discord.py API wrapper.
The bot uses the one with voice support, but it currently does not have voice features yet.

https://github.com/Rapptz/discord.py

requests module is also needed.

## Setup

You'll need to install requests and discord.py module.

Add your token at the end of the Python file, complete with ''.

## Current Features

Prefix is m!.

!say args

    Makes the bot say the supplied argument.

!dere arg1 arg2

    Valid arg1 arguments:

      player : displays a small image summarizing player statistics.

      master : returns how much the player cleared and got Full Combo on master charts.

    Valid arg2 argument can only be 9 digit Deresute ID.

!mltd arg1 arg2

    Valid arg1 arguments:

      current : returns current Mirishita version.

      date : returns last version's update date.

      event : returns event information according to arg2

    Valid arg2 arguments:

      name : returns event name.

      type : returns event type.
!github

    Links to this github.
