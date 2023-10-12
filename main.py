import discord
from discord.ext import commands
import random


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready(ctx):
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy {bot.user}, estoy para ayudar, utiliza $help para ver el menu de ayuda.')

@bot.command()
async def debug(ctx):
    await ctx.send(random.randint(1,120930129301920391029301))

@bot.command()
async def bhelp(ctx):
    await ctx.send("hello : saluda al bot - bhelp : abre este menu - spam : spamea un texto - debug : testea si el bot esta activo")

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def spam(ctx):
    await ctx.send("holaaaaaaaa " * 3)

bot.run("TOKEN")
