import discord
from discord.ext import tasks


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        self.auto_yee.start()
        await self.change_presence(activity=discord.Game(name="yee"))

    async def on_message(self, message):
        if message.author == self.user:
            return
        if "yee" in message.content:
            await message.channel.send('yee <:uhh:1038524509646503946>')
            
    @tasks.loop(hours=1.0)
    async def auto_yee(self):
        channel = await client.fetch_channel('1087365546380628069')
        await channel.send('yee!')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents = intents)
client.run('#')