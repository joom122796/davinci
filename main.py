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
async def davinci(
  ctx,
  lang: discord.Option(str, description='Specified programming language', choices=['Python','JS','Ruby','Go','Perl','Swift','TypeShift','SQL','Shell','C#'], required=True),
  task: discord.Option(str, description='Natural language task', required=True),
):
  openai.api_key = os.getenv("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")
  response = openai.Completion.create(
    model='text-davinci-002',
    prompt = f'{lang} \n{task}',
    temperature = 0.7,
    max_tokens = 256,
    top_p = 1,
    frequency_penalty = 0,
    presence_penalty = 0
  )
  await ctx.send(f'```{response}```')

@bot.slash_command(description='Get Bitcoin wallet address information')
async def btcaddress(interaction: Interaction, address: str):
  api = requests.get(f'https://chain.api.btc.com/v3/address/{address}')
  data = api.json()
  inc = data['received']
  outc = data['sent']
  bal = data['balance']
  embd = discord.Embed(title=f'Bitcoin address lookup: {address}',description=f'Balance: {bal} \nAmount received: {inc} \nAmount spent: {outc}')
  embd.set_footer(text='不劳而获的收获')
  await interaction.send(embed=embd)

@bot.slash_command(description='Get Bitcoin transfer information')
async def btctransac(interaction: Interaction, TransactionID: str):
  api = requests.get(f'https://chain.api.btc.com/v3/tx/{TransactionID}')
  data = api.json()
  hash = data['hash']
  creationTime = data['created_at'] 
  confirm = data['confirmations']
  embd = discord.Embed(title=f'Bitcoin transaction lookup:{TransactionID}',description =f'Creation Time: {creationTime} \nConfirmations: {confirm}')
  embd.set_footer(text=f'{hash} \n不劳而获的收获')
  await interaction.send(embed=embd)
  
bot.run('')
