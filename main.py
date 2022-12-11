from source.utils.basic_commands import BasicCommands
from source.utils.settings import Login, Settings
from source.utils.tools import idtoarobase
from source.account import Account
from source.giver import Giver

from discord.ext import commands
from discord.ext.commands.context import Context

import discord


intents = discord.Intents.default()
intents.message_content = True
login = Login.load(False)
bot = commands.Bot(command_prefix="$", intents=intents)
basic = BasicCommands()
settings = Settings()


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=settings.statut))


@bot.command(name='ping')
async def ping(ctx: Context):

    message = basic.get('ping', [idtoarobase(
        ctx.author.id), round(bot.latency * 1000)])
    await ctx.send(message)


@bot.command(name='dev')
async def dev(ctx: Context):

    embed = discord.Embed(
        title="Credits", description="A quick list of my designer :technologist:", color=0xb75800)

    embed.add_field(name="__Statut__  :x:", value="Currently in dev")
    embed.add_field(name="Main Developer", value=idtoarobase(
        669530329299550218), inline=False)
    embed.add_field(name="Library", value="`discord.py`", inline=False)
    embed.set_thumbnail(url=bot.user.avatar.url)

    await ctx.send(embed=embed)


@bot.command(name='register')
async def register(ctx: Context):

    if settings.functionnalities['register'] == False:
        await ctx.author.send(basic.get('register.disable', [idtoarobase(ctx.author.id)]))
    else:
        Account.new_account(ctx.author.id, ctx.author.name)
        await ctx.author.send(basic.get('register.successful', []))


@bot.command(name="distribute")
@commands.is_owner()
async def distribute(ctx: Context):
    Giver.distribute()
    await ctx.send(basic.get('distribution.successful', [idtoarobase(ctx.author.id)]))


@bot.command(name='getmysecret')
async def getmysecret(ctx: Context):

    if settings.functionnalities['write_message'] == False:
        await ctx.author.send(basic.get('write.disable', [idtoarobase(ctx.author.id)]))
    else:
        await ctx.author.send(basic.get('secret.who', [Account.get_receiver(str(ctx.author.id))[1]]))

@bot.command(name='write')
async def write(ctx: Context, message: str): 

    target = Account.get_receiver(str(ctx.author.id))[1]

    if settings.functionnalities['write_message'] == False:
        await ctx.author.send(basic.get('write.disable', [idtoarobase(ctx.author.id)]))
    else :  
        Account.write_message(str(ctx.author.id), message)
        embed = discord.Embed(
            title=f"Message pour {target}", description=message, color=0x00dd00
        )
        await ctx.author.send(embed=embed)

@bot.command(name='readmine')
async def readmine(ctx: Context): 
    
    target = Account.get_receiver(str(ctx.author.id))[1]
    message = Account.get_message(str(ctx.author.id))

    if settings.functionnalities['write_message'] == False:
        await ctx.author.send(basic.get('write.disable', [idtoarobase(ctx.author.id)]))
    else :  
        embed = discord.Embed(
            title=f"Message pour {target}", description=message, color=0xff0000
        )
        await ctx.author.send(embed=embed)

@bot.command(name='christmasread')  
async def christmasread(ctx: Context): 

    if settings.functionnalities['read_message'] == False:
        await ctx.author.send(basic.get('read.disable', [idtoarobase(ctx.author.id)]))
    else : 
        message = Account.get_secret_message(str(ctx.author.id))
        embed = discord.Embed(
            title=f"Message pour {ctx.author.name}", description=message, color=0xff0000
        )
        embed.set_footer(text="De la part d'un admirateur secret")
        await ctx.author.send(embed=embed)

@bot.command(name='getmembers')
async def getmembers(ctx: Context): 

    members_list = Account.get_members()

    embed = discord.Embed(
        title = "Une liste de tout les membres inscrit apparaît !", description="Lisons ça de prêt...:guigui2_hehe:", color=0x0000dd
    )
    for element in members_list : 
        embed.add_field(name=element, value="🎁", inline=False)
    
    await ctx.send(embed=embed)

@bot.command(name='changefunc')
@commands.is_owner()
async def changefunc(ctx: Context, f_name, f_value) : 
    settings.change_functionnalities(f_name, bool(int(f_value)))
    await ctx.send(f"Value of `{f_name}` is now on {settings.functionnalities[f_name]}")


bot.run(login['token'])
