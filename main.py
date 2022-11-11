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
  
@bot.slash_command(description='Use Davinci to transform natural language into code. Use /support to see supported languages')
async def davinci(
  ctx,
  lang: discord.Option(str, choices=['py','js','go','rb','cs','pl','swift','sql','shell','typeshift'], required=True),
  task: discord.Option(str, required=True)
):
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
  length = {len(response["choices"][0])}
  if length > 2000:
    with open('response.txt', 'w') as f:
      f.write(f'{response["choices"][0]}')
    with open('response.txt', 'rb') as file:
      if lang == 'shell' or lang == 'typeshift':
        await interaction.respond(file=discord.File(file, f'response.txt'))
      else:
        await interaction.respond(file=discord.File(file, f'response.{lang}'))
  else:
    await interaction.respond(f'```\n{lang} \n{response["choices"][0]}```')

@bot.slash_command(description='Displays full list of Codex supported languages')
async def support(interaction: Interaction):
  embd = discord.Embed(title='**CODEX SUPPORTED LANGUAGES**',description=f'\n- Python (most efficient) \n- JavaScript \n- Go \n- Ruby \n- C# \n- Perl \n- Swift \n- SQL \n- Shell \n- TypeShift \n\n\nNote: Attachments are not supported for Shell or TypeShift programs, therefore .txt files are their default format')
  embd.set_author(discord.ApplicationContext.author)
  embd.set_footer(text='不劳而获的收获')
  await interaction.send(embed=embd)
    
bot.run('MTA0MDM3NDE2NzU3MDIzOTUwOA.G30w6M.z05rxA2pUD3StbfkjYDTs6gEO-iSd-Yu6B8F3s')
