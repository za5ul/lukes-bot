import discord
from discord.utils import get
import time

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()




rolen_verteiler_channel_id = 889427272094855188

class MyClient(discord.Client):
    # einloggen
    async def on_ready(self):
        print('Ich bin jetzt da')

        rolen_channel = client.get_channel(rolen_verteiler_channel_id)
        await rolen_channel.send('Moin, bitte reagiere auf die Rollen, die du haben willst \n'
                                 '🟧 = cool\n'
                                 '⬛ = mega schlau\n'
                                 '🟦 = Server-DJ')

    async def on_reaction_add(self, reaction, user):
        cool = discord.utils.get(user.guild.roles, name='cool')
        megaschlau = discord.utils.get(user.guild.roles, name='mega schlau')
        dj = discord.utils.get(user.guild.roles, name='Server-DJ')


        if str(reaction.emoji) == '🟧':
            await user.add_roles(cool)

        if str(reaction.emoji) == '⬛':
           await user.add_roles(megaschlau)

        if str(reaction.emoji) == '🟦':
           await user.add_roles(dj)



    async def on_member_join(member, user):
        pass


    async def on_member_remove(member):
        pass




    #wenn nachricht gepostet wird
    async def on_typing(self, user, channel, when):
        print(str(user) + 'tippt gerade in' + str(channel) + 'channel seit' + str(when))

    async def on_message_delete(self, message):
        bericht1 = ('Gelöschte Nachricht: '+ str(message.content)+' '+'|: '+ str(message.author)+' '+'|: '+str(message.channel)+' '+'|: '+str(message.guild))
        datei = open('spy.txt','a')
        datei.write(bericht1+'\n')
        datei.close()

    async def on_message_edit(self, before, after):
        bericht2 = ('Geaenderte Nachricht: '+' '+ before.content +' '+'|GEÄNDERT ZU|' +' '+ after.content)
        datei = open('spy.txt', 'a')
        datei.write(bericht2+'\n')
        datei.close()


    async def on_member_update(self, before, after):
        pass
        #roles = discord.utils.get(after.guild.roles, name='test role')
        #await after.add_roles(roles)

    async def on_message(self, message):
        if message.author == client.user:
            return

        bericht3 = ('Normale Nachricht: '+' '+str(message.content)+' '+ ' |: '+' '+str(message.author)+' '+'|: '+str(message.channel)+' '+'|: '+str(message.guild))
        datei = open('spy.txt', 'a')
        datei.write(bericht3 + '\n')
        datei.close()

        gruss_liste = ['hey', 'hi', 'moin', 'Moin','tach']
        gruss_bot = ['Moin', 'Grüß Gott', 'Hey', 'Grüß dich']

        # musik abspielen (noch nicht fertig)
        if message.content.startswith('!play'):
            where = message.content.split(" ")[1]
            channel = get(message.guild.channels, name=where)
            voicechannel = await channel.connect()
            voicechannel.play(discord.FFmpegPCMAudio('9er Alpenjäger.mp3'))
            while voicechannel.is_playing():
                time.sleep(5)
            voicechannel.play(discord.FFmpegPCMAudio)
            if voicechannel.is_paused():
                pass
            voicechannel.stop()
            voicechannel.pause()
            voicechannel.resume()

        if message.content.startswith(''):
            pass


        if message.content.startswith(str(gruss_liste)):
            await message.content.send(str(gruss_bot)+ ', ' +message.author)
        if message.content.startswith('!gruss'):
            await message.channel.send('Sei gegrüßt, Kamerad!')

        if message.content.startswith('!hilfe'):
            await message.channel.send('```!gruss = Gruß vom Bot\n'
                                       '!lastm = die letzten 10 Nachrichten\n'
                                       '!chatwithme = Bot chattet mit dir\n'
                                       '!tester = Zeigt die akutellen Tester\n'
                                       '!insta = zum Insta Kanal des Owner\n'
                                       '!antrag = Erklärt dir, wo du dein Antrag machen kannst\n'
                                       ''
                                       '!smile = ein lächeln vom Bot```')

        if message.content.startswith('!lastm'):
            messages = await message.channel.history(limit=10).flatten()
            for i in messages:
                await message.channel.send(str(i.content))

        if message.content.startswith('!tester'):
            await message.channel.send('Aktuelle Tester sind: Keiner')

        if message.content.startswith('!insta'):
            await message.channel.send('Folge mir gerne auf Insta: @dukelvke')

        if message.content.startswith('!chatdata') and str(message.author) == 'DukeLvke#1111':
            try:
                await message.channel.send(file=discord.File('chat.txt'))
            except:
                if str(message.author) != 'DukeLvke#1111':
                    await message.channel.send('Dazu bist du nicht befugt!')



















client = MyClient()
client.run(token)
