import discord
import asyncio
from discord import channel
from discord.utils import get
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
client2 = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print('logged in as')

@client.event
async def on_member_join(member):
    channel = client.get_channel(782228216554455070)
    await channel.send(f'Hello <@{member.id}>, Merhba bik M3ana')
    role = get(member.guild.roles, id=893976972890370048)
    await member.add_roles(role)


@client.event
async def on_voice_state_update(member,before, after):
    channel = client.get_channel(904467050104254545)
    if not before.channel and after.channel:
        await channel.send(f'<@{member.id}>  joined **{after.channel}**')
        # print(f'{member} has  joined {after.channel}')
    elif not after.channel and before.channel:
        await channel.send(f'<@{member.id}> left **{before.channel}**')



@client2.command
async def test(ctx):
    print("test")


client.run('OTAzOTk3OTQ4OTQ4NTQ1NTY2.YX1Hsg.e6RIzXLQduqm9OGyDCCvcDCP-vY')