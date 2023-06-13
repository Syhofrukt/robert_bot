import discord
from discord.utils import get
from discord.ext import commands
import asyncio

class Visuals(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author != self.bot.user:
            if message.content == '!heart':
                channel = message.channel
                await channel.send(":white_large_square::white_large_square::black_large_square::black_large_square::white_large_square::white_large_square::white_large_square::black_large_square::black_large_square::white_large_square::white_large_square:")

        if message.author == self.bot.user:
            list_heart = [
                "\n:white_large_square::black_large_square::red_square::red_square::black_large_square:"
                ":white_large_square::black_large_square::red_square::red_square::black_large_square:"
                ":white_large_square:",

                "\n:black_large_square::red_square::white_large_square::white_large_square::red_square:"
                ":black_large_square::red_square::red_square::red_square::red_square::black_large_square:",

                "\n:black_large_square::red_square::white_large_square::red_square::red_square::red_square:"
                ":red_square::red_square::red_square::red_square::black_large_square:",

                "\n:black_large_square::red_square::red_square::red_square::red_square::red_square::red_square:"
                ":red_square::red_square::red_square::black_large_square:",

                "\n:white_large_square::black_large_square::red_square::red_square::red_square::red_square:"
                ":red_square::red_square::red_square::black_large_square::white_large_square:",

                "\n:white_large_square::white_large_square::black_large_square::red_square::red_square:"
                ":red_square::red_square::red_square::black_large_square::white_large_square::white_large_square:",

                "\n:white_large_square::white_large_square::white_large_square::black_large_square::red_square:"
                ":red_square::red_square::black_large_square::white_large_square::white_large_square:"
                ":white_large_square:",

                "\n:white_large_square::white_large_square::white_large_square::white_large_square:"
                ":black_large_square::red_square::black_large_square::white_large_square::white_large_square:"
                ":white_large_square::white_large_square:",

                "\n:white_large_square::white_large_square::white_large_square::white_large_square:"
                ":white_large_square::black_large_square::white_large_square::white_large_square:"
                ":white_large_square::white_large_square::white_large_square:"
            ]

            for line in list_heart:
                await asyncio.sleep(1)
                await message.edit(content=message.content + line)




async def setup(bot):
    await bot.add_cog(Visuals(bot))
