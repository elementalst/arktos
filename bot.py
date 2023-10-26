import discord
from discord.ext import commands

TOKEN = "TOKEN HERE"

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name="ping", description="Get bot's ping")
async def ping(ctx):
    # Respond to a /ping slash command with the bot's latency (ping) in milliseconds.
    latency = round(bot.latency * 1000)
    await ctx.respond(f'Pong! Latency: {latency}ms')

bot.run(TOKEN)
