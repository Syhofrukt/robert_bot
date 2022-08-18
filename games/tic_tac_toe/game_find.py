from discord.ext import commands


class GameFinder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author != self.bot.user:
            if message.content.startswith('!pingpong'):
                guild = message.guild
                channel = message.channel
                members = guild.members
                for member in members:
                    if member != message.author:
                        if message.content.startswith('!pingpong ' + member.mention):
                            await channel.send('{}, вы начали игру в Пинг Понг с пользователем {}!'
                                               .format(message.author.mention, member.mention))
                            break


async def setup(bot):
    await bot.add_cog(GameFinder(bot))
