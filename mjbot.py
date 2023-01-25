#!/usr/bin/env python3

import discord
import spacy
import re
import logging
import os

tester = re.compile("doing", flags=re.IGNORECASE)
matcher = re.compile(r"\bdoing ([^\n\.?!]{3,})", flags=re.IGNORECASE)
partialemote = re.compile(r"(<a?:[A-z0-9-_]{2,32}:[0-9]{8,19}$)|(<(@|#|@&)!?[0-9]{8,19}$)") # For fixing an issue where the last > of an emoji or ping code gets cut off
helpstring = re.compile("<@iothwei9outhwnebstgwesi8o9thwu3s4eitgwy8iu94o5yh5twi4se.;/t>") # This is just gibberish because it will be overwritten later, and I don't want it to match anything until then
helpembed = {
    "title": "MJ Bot",
    "type": "rich",
    "description": "I'm stuff",
    "color": 7419530,
    "thumbnail": {"url": "https://cdn.discordapp.com/attachments/366776253124050947/848069294637056000/mj_is_stuff.jpg"},
    "fields": [{
        "name": "About",
        "value": """
        MJ Bot is a bot which critics are calling "a bot". What does it do, you're asking yourself? Well, when a user sends a message with the word "doing" in it, the bot reenacts the popular "I'm stuff" meme which all the cool kids are talking about, featuring Tony Stark and Robert Downey Jr. from the hit film "Avenger". That's about it, but it's a lot of fun for the whole family to enjoy.

        This bot is intended to be a replacement for [the original](https://top.gg/bot/606268348380086370), which no longer seems to be operating. However, it doesn't behave the same as the original, as I never actually got to see it in action.
        """
    }, {
        "name": "Links",
        "value": "[Bot Invite Link](https://discord.com/api/oauth2/authorize?client_id=848031245619036221&scope=bot) | [GitHub](https://github.com/saucylegs/mjbot)"
    }]
}

logging.basicConfig(level=logging.WARNING)
nlp = spacy.load("en_core_web_sm")
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    global helpstring
    helpstring = re.compile(f"<@!?{client.user.id}> help")
    print(f"Bot is in {len(client.guilds)} servers")
    await client.change_presence(activity=discord.Game("I'm stuff"))


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.guild and message.channel.permissions_for(message.guild.me).send_messages == False:
        return
    
    match = matcher.search(message.content)
    if match:
        text = match.group(1)
        doc = nlp(match.group(0))
        chunks = []
        for chunk in doc.noun_chunks:
            chunks.append(str(chunk))

        if len(chunks) < 1:
            reply = text
        else:
            position = text.find(chunks[0]) + len(chunks[0])
            reply = text[0:position]
            if partialemote.search(reply):
                reply += ">"

        await message.reply(f"I'm {reply}")

    elif helpstring.match(message.content) or (type(message.channel) == discord.DMChannel and message.content.lower() == "help"):
        await message.reply(embed=discord.Embed.from_dict(helpembed))


client.run(os.environ["TOKEN"])
