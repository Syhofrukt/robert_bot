#Код если я вдруг захочу делать игру на много человек с набором



import discord
import asyncio

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


player_list = []

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    channel = message.channel

    if message.content.startswith('$hello'):
        await channel.send('Hello!')

@client.event
async def on_message(message):
    channel = message.channel
    members = channel.guild.members

    if message.content == '!pingpong':
        await channel.send('{}, вы начали набор в игру Пинг Понг. Чтобы присоединится к игре,'
                                          ' противник должен написать !game с упоминанием '
                                          'игрока запросившего поиск игры (через пробел). Также вы можете написать '
                                          '!game с упоминанием игрока (через пробел), с которым вы хотите сыграть'
                                          .format(message.author.mention), reference=message)

        def check(message1):
            for member in members:
                if member != message1.author:
                    if message1.content.startswith('!game ' + member.mention):
                        player_list.append(message1.author)
                        player_list.append(member)
                        break

            if message1.content.startswith('!game ' + message.author.mention) and message1.author != message.author:
                player_list.append(message.author)
                player_list.append(message1.author)
            return True

        while True:
            try:
                await client.wait_for('message', timeout=120.0, check=check)
            except asyncio.TimeoutError:
                await channel.send('{}, время набора истекло'.format(message.author.mention), reference=message)
                break
            else:
                try:
                    await channel.send(
                        '{}, вы играете против игрока {}'.format(player_list[0].mention, player_list[1].mention))
                except IndexError:
                    break
                else:
                    break

client.run('MTAwODQzMDE0NzcyMjAyNzAwOA.G5lphK.nU5ETEbRY4AxnwiCWIegBfCCzQiHYJVmTCh6Lk')