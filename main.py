import discord
from discord.ext import commands

client = commands.Bot(help_command=None) #intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f"Online as {client.user.name}#{client.user.discriminator}")

@client.user_command(name="Mald", guild_ids=[1026676957280206879])
async def mald(ctx, target: discord.Member):
    if target.id == ctx.author.id:
        return await ctx.respond(f"You can't mald yourself.")
    if not target.voice:
        return await ctx.respond(f"{target.mention} is not in a voice channel.")

client.run(open("token","r").read())