import discord
import asyncio
from discord.utils import get

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('logged in as')

@client.event
async def on_member_join(member):
    channel = client.get_channel(782228216554455070)
    await channel.send(f'Hello <@{member.id}>, Merhba bik M3ana')
    role = get(member.guild.roles, id=893976972890370048)
    await member.add_roles(role)



client.run('OTAzOTk3OTQ4OTQ4NTQ1NTY2.YX1Hsg.MR0woOjr3wniE-qX_JeAqEkcwiw')