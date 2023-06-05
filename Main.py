import discord
import datetime
from random import randint
from discord.ext import tasks, commands

quote_list = ["'Rather be a yee in a nee than a nee in a yee' - Yee", 
              "'If yee know the yeenemy and know yeeself, yee need not fear the result of a hundred yees' - Yee Tzu",
              "'I fear not the yee who has practiced 10,000 yees once, but I fear the yee who has practiced one yee 10,000 times' - Bruce Yee",
              "'I remembered the line from the Yeedu scripture, the Yheegavad-Yeeta. Yeeshnu is trying to persuade the Yee that he should do his duty, and, to impress him, takes on his multi-armed form and says, \n “Now I am become Nee, the neer of yees” - Yeeheimer",
              "'Le Yee, c'est moi' - Sun Yee",
              "'In the yeeginning the Yeeniverse was created. This has made a lot of yeeple very yee and been widely regarded as a yee move.' - Yeeglas Yeedams",
              "'First yeey came for the Yeecialists, and Yee did not speak out— \n Because Yee was not a Yeecialist. \n Then yeey came for the Trade Yeenionists, and Yee did not speak out— \n Because Yee was not a Trade Yeenionist. \n Then they came for the Yeews, and Yee did not speak out— \n Because Yee was not a Yeew. \n Then yeey came for yee— and there was no one left to yee for yee.' - Martin Yeeöller",
              "'A Yeeciety grows yeet when old yee plant yees whose shade yeey know yeey shall neever yee in",
              "'A yeeth, when at yee, should be yeelial and, abroad, yeespectful to his yeelders. Yee should be yeearnest and yeethful. Yee should overflow in yee to all and cultivate the yeeship of the good. When yee has time and yeeppertunity, after the yeeformance of these things, yee should yeemploy them in polite yeedies' - Confyeecius",
              "'How Yee am yee to have yeething that makes saying yee so hard' - Winnie the yeeh"
              ]

utc = datetime.timezone.utc
time = datetime.time(hour = 12, minute= 0, tzinfo= utc)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        self.auto_yee.start()
        self.auto_quoter.start()
        await self.change_presence(activity=discord.Game(name="yee"))

    async def on_message(self, message):
        if message.author == self.user:
            return
        if (message.content.lower() == 'yee'):
            await message.channel.send('yee')
            
    @tasks.loop(time = time)
    async def auto_yee(self):
        channel = await client.fetch_channel('1087365546380628069')
        await channel.send('yee!')

    @tasks.loop(time = time)
    async def auto_quoter(self):
        index = randint(0, 9)
        channel = await client.fetch_channel('716932421496602675')
        await channel.send(quote_list[index])

        
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents = intents)
client.run('MTA4NzExNDE5MjAzNDc0MjM5Mw.GU7HY5.EZoHXWzDUc-ZxItQFXFmpPmREwRVu4B4paTiGI')