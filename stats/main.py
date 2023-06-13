import discord
from discord.utils import get
from discord.ext import commands
import asyncio


class Statistics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        while True:
            guilds_list = self.bot.guilds
            for server in guilds_list:
                if get(server.categories, name='Статистика сервера') is not None:
                    for channel in server.voice_channels:
                        if channel.name.startswith('Всего участников:'):
                            await channel.edit(name='Всего участников: {}'.format(server.member_count))
                        if channel.name.startswith('Онлайн:'):
                            users_online = 0
                            for member in server.members:
                                if member.status == discord.Status.online or member.status == discord.Status.dnd:
                                    users_online += 1
                            await channel.edit(name='Онлайн: {}'.format(users_online))
                        if channel.name.startswith('Ботов:'):
                            bots = len([discord.utils.get(server.members, bot=True)])
                            await channel.edit(name='Ботов: {}'.format(bots))
            await asyncio.sleep(300)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author != self.bot.user:
            if message.content == '!$create_stats':
                if message.author.guild_permissions.administrator is True:
                    guild = message.guild
                    categoryy = get(guild.categories, name='Статистика сервера')
                    if categoryy is None:
                        everyone = guild.default_role
                        permissions = discord.PermissionOverwrite.from_pair(deny=discord.Permissions.all(), allow=[])
                        overwrites = {everyone: permissions}
                        permissions.update(view_channel=True)
                        category = await guild.create_category_channel('Статистика сервера', position=0)
                        await guild.create_voice_channel('Всего участников: ', overwrites=overwrites, category=category)
                        await guild.create_voice_channel('Онлайн: ', overwrites=overwrites, category=category)
                        await guild.create_voice_channel('Ботов: ', overwrites=overwrites, category=category)

# Когда нибудь потом
            # if message.content == '!$custom_stats':
            #     guild = message.guild
            #     channel = message.channel
            #     await channel.send('Выберите текст для каждой строчки таблицы, и значение которое будет вычислятся '
            #                        '(колличество пользователей с определенной ролью или просто общее значение пользователей в сети')


async def setup(bot):
    await bot.add_cog(Statistics(bot))
