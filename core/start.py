import discord
from discord.utils import get
import time

intents = discord.Intents.all()
client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    while True:
        guilds_list = client.guilds
        for server in guilds_list:
            if get(server.categories, name='Статистика сервера') is not None:
                for channel in await discord.utils.get(server.voice_channels):
                    if channel.name.startswith('Всего участников:'):
                        await channel.edit(name='Всего участников: {}'.format(server.member_count))
                    if channel.name.startswith('Онлайн:'):
                        for member in server.members:
                            users_online = 0
                            if member.status == discord.Status.online or member.status == discord.Status.dnd:
                                users_online += 1
                            await channel.edit(name='Онлайн: {}'.format(users_online))
                    if channel.name.startswith('Ботов:'):
                        bots = len(await discord.utils.get(server.members, bot=True))
                        await channel.edit(name='Ботов: {}'.format(bots))
        time.sleep(300)

@client.event
async def on_message(message):
    if message.author != client.user:
        guild = message.guild
        channel = message.channel
        members = guild.members

        if message.content.startswith('!pingpong'):
            for member in members:
                if member != message.author:
                    if message.content.startswith('!pingpong ' + member.mention):
                        await channel.send('{}, вы начали игру в Пинг Понг с пользователем {}!'
                                           .format(message.author.mention, member.mention))
                        break

        if message.content == '!$create_stats':
            if message.author.guild_permissions.administrator is True:
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

client.run('MTAwODQzMDE0NzcyMjAyNzAwOA.G5lphK.nU5ETEbRY4AxnwiCWIegBfCCzQiHYJVmTCh6Lk')