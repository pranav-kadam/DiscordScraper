import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

bot_token = ''
guild_id = ''

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    guild = bot.get_guild(int(guild_id))
    
    if guild is not None:
        # Get the total number of members in the server
        online_members = sum(1 for member in guild.members if member.status == discord.Status.online)
        print(f'Active Members: {online_members}')

        # You can access specific channels by their name or ID
        for channel in guild.text_channels:
            channel_message_count = 0  # Initialize message count
            async for message in channel.history(limit=None):
                channel_message_count += 1
            print(f'Messages in {channel.name}: {channel_message_count}')
    else:
        print(f"Bot is not in the server with ID {guild_id}")

bot.run(bot_token)