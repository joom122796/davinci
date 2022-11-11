import os
import openai
import requests
import discord
from discord import Interaction
from discord.ext import commands 

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
  print('Online')
  await bot.change_presence(status=discord.Status.dnd)
  
@bot.slash_command(description='Use Davinci to transform natural language into code.')
async def davinci(interaction: Interaction, lang: str, task: str):
  openai.api_key = ("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")
  response = openai.Completion.create(
    model='code-davinci-002',
    prompt = f'{lang} {task}',
    temperature = 0.7,
    max_tokens = 8000,
    top_p = 1,
    frequency_penalty = 0,
    presence_penalty = 0
  )
  await interaction.respond(f'```{response["choices"][0]}```')

bot.run('MTA0MDM3NDE2NzU3MDIzOTUwOA.G30w6M.z05rxA2pUD3StbfkjYDTs6gEO-iSd-Yu6B8F3s')
