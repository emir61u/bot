import discord
from discord.ext import commands
from algi import model
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)



@bot.command()
async def kontrol(ctx):
    if ctx.message.attachments:
        for resim in ctx.message.attachments:
            resim_ismi =resim.filename
            resim_url = resim.url
            await resim.save(f"./{resim.filename}")
            await ctx.send(f"Resim başarıyla kaydedildi./{resim.filename}")
            await ctx.send(model(models="./keras_model.h5", etiket="labels.txt",resim=f"./{resim.filename}"))
            print(models="./keras_model.h5", etiket="labels.txt",resim=f"./{resim.filename}")
    else:   
        await ctx.send("Fotoğraf eklemeniz gerekiyor")







bot.run("")