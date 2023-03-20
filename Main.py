import discord
import datetime
from discord.ext import tasks, commands


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        self.auto_yee.start()
        await self.change_presence(activity=discord.Game(name="yee"))

    async def on_message(self, message):
        if message.author == self.user:
            return
        if (message.content == 'yee') or (message.content =='Yee'):
            await message.channel.send('yee')
            

    @tasks.loop(hours=8.0)
    async def auto_yee(self):
        channel = await client.fetch_channel('channel')
        await channel.send('yee!')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents = intents)
client.run('TOKEN')