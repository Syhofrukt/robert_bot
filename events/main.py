from discord.ext import commands
import sqlite3
from schemas import insert
import uuid
import threading


class EventCreator(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.filename = ''
        self.con = sqlite3.connect(self.filename)

    def get_connection(self):
        cur = self.con.cursor()
        return cur

    def insert_into_table(self, info_list: list):
        self.get_connection().executemany("INSERT INTO Events VALUES(?, ?, ?, ?, ?)", info_list)

    @commands.Cog.listener()
    async def on_ready(self):
        self.filename = 'events.db'

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author != self.bot.user:
            if message.content.startswith('!event_create'):
# НУЖНО ПРОВЕРЯТЬ ПРАВА АВТОРА СООБЩЕНИЯ, ДЛЯ ТОГО ЧТОБЫ СДЕЛАТЬ СОБЫТИЕ
                message_el = message.content.split()
                date = message_el[2].split('.')
                time_lst = message_el[3].split(':')
                id = uuid.uuid4()

                insert_data_class = insert.InsertDataModel(key=id, name=message_el[1], day=int(date[0]),
                                                           month=int(date[1]), year=int(date[2]), hour=int(time_lst[0]),
                                                           minute=int(time_lst[1]))
                channel = message.channel
                info_list = [insert_data_class.key, insert_data_class.name, insert_data_class.day,
                             insert_data_class.month, insert_data_class.year, insert_data_class.hour,
                             insert_data_class.minute, message.author, channel.server]

                thread1 = threading.Thread(target=self.insert_into_table, args=(info_list,), daemon=True)

                await channel.send('{}, вы создали новое событие на {} которое будет исполняться в {}'
                                   .format(message.author.mention, message_el[2], message_el[3]))


async def setup(bot):
    await bot.add_cog(EventCreator(bot))






