import discord
from discord.ext import commands
import asyncio


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


extensions = ['stats.main', 'games.tic_tac_toe.game_find']


async def main():
    async with bot:
        for extension in extensions:
            await bot.load_extension(extension)

        await bot.start('MTAwODQzMDE0NzcyMjAyNzAwOA.Gpr9q9.BgTTQlLH1GOTBepmaAIfjHNGzjCw4wpaWtF3Yw')





@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_message(message):
    pass

asyncio.run(main())
