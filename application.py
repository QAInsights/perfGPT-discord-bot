import os
import logging
import discord
import constants

from dotenv import load_dotenv
from openai_engine import ask_openai
from utils import pop_conversation

load_dotenv()
logging.basicConfig(level=logging.INFO)

token = os.getenv("DISCORD_TOKEN")
my_guild = os.getenv("DISCORD_GUILD")

intents = discord.Intents.all()
client = discord.Client(intents=intents)

previous_conversation_response = [constants.initial_conversation]


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == my_guild:
            break

    print(
        f"{client.user} is connected to the following guild:\n"
        f"{guild.name}(id: {guild.id})"
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    user_input = message.content.lower()

    logging.info(previous_conversation_response[-1])

    response = ask_openai(user_input=user_input,
                          previous_conversation_response=previous_conversation_response)
    logging.info(response[1])

    pop_conversation(previous_conversation_response)
    await message.channel.send(str(response[0]))

client.run(token)
