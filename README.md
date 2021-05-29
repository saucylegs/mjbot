# MJ Bot
I'm stuff

## About
MJ Bot is a Discord bot which critics are calling "a bot". What does it do, you're asking yourself? Well, when a user sends a message with the word "doing" in it, the bot reenacts the popular "I'm stuff" meme which all the cool kids are talking about, featuring Tony Stark and Robert Downey Jr. from the hit film "Avenger". That's about it, but it's a lot of fun for the whole family to enjoy.

This bot is intended to be a replacement for [the original](https://top.gg/bot/606268348380086370), which no longer seems to be operating. However, it doesn't behave the same as the original, as I never actually got to see it in action.

## Invite
[Invite MJ Bot to your Discord server](https://discord.com/api/oauth2/authorize?client_id=848031245619036221&scope=bot)

## Technical details
This version of MJ Bot is written in Python and uses the [spaCy natural language processing library](https://spacy.io/). The purpose of the NLP library is to identify noun phrases so that the bot doesn't send back anything extraneous (e.g. if you say "I'm going to be doing your mom tomorrow", the bot will respond "I'm your mom" instead of "I'm your mom tomorrow"). Is this overkill for this stupid joke bot? Yes, but you know what they say, "YOLO ('You Only Live Once')"

### Running the bot
If you want to run the bot yourself, you need to have the latest version of Python 3, and the [discord.py](https://discordpy.readthedocs.io/en/latest/index.html) and the [spaCy](https://spacy.io/usage) libraries installed.

Once you have gotten those set up, and the mjbot.py file is downloaded too, the bot can be started with the command:
```bash
TOKEN='your bot token from https://discord.com/developers/applications here' python mjbot.py
```
