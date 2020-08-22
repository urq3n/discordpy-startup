import discord
import asyncio
import time

class tunatuna(discord.Client):
    async def on_ready(self): #ログイン情報
        print("やせいのつなでがあらわれた。")
        CHANNEL_ID = 646339519322390580
        channel = client.get_channel(CHANNEL_ID)
        await channel.send("やせいのつなでがあらわれた。")
        await client.change_presence(activity=discord.Game(name="🥫🐟"))
    
    async def on_message(self, message):
        if message.author == self.user: #botかどうか判断
            return

        if "つなで" in message.content: #あいさつ再生
                await message.channel.send("wow wow")
                vc =await discord.VoiceChannel.connect(message.author.voice.channel)
                vc.play(discord.FFmpegPCMAudio("music\BOT.mp3"), after=lambda e: print(e ))
                await asyncio.sleep(3.0)
                vc.stop()
                await vc.disconnect()

        if message.content == "bow wow": #あいさつ再生
                vc =await discord.VoiceChannel.connect(message.author.voice.channel)
                vc.play(discord.FFmpegPCMAudio("music\Bow wow.mp3"), after=lambda e: print(e ))
                await asyncio.sleep(8.3)
                vc.stop()
                await message.delete()
                await vc.disconnect()   

        if message.content == "wow wow": #あいさつ再生
                vc =await discord.VoiceChannel.connect(message.author.voice.channel)
                vc.play(discord.FFmpegPCMAudio("music\wow wow.mp3"), after=lambda e: print("", e ))
                await asyncio.sleep(3.2)
                vc.stop()
                await message.delete()
                await vc.disconnect()

        if "ww" in message.content:  #wを含むと再生
                vc =await discord.VoiceChannel.connect(message.author.voice.channel)
                vc.play(discord.FFmpegPCMAudio("music\warai.mp3"), after=lambda e: print("", e ))
                await asyncio.sleep(3.2)
                await message.delete()
                vc.stop()
                await vc.disconnect()    
        
        if message.content == "つなぱっぱや": #あいさつ再生
                vc =await discord.VoiceChannel.connect(message.author.voice.channel)
                vc.play(discord.FFmpegPCMAudio("music\pappaya.mp3"), after=lambda e: print("", e ))
                vc.source = discord.PCMVolumeTransformer(vc.source)
                vc.source.volume = 0.5
                await asyncio.sleep(27.2)
                vc.stop()
                await message.delete()
                
                await vc.disconnect()
        
client = tunatuna()
client.run("NzQ2NzExNjA0MjQ2MjE2NzQ0.X0ETXw.rOoUuYPDcnuAtlrrdyc3p8iebwI")