import discord
import random
from discord.ext import commands

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password


def caraoucoroa():
    moeda= random.randint(0, 2)
    if moeda == 0:
        return "cara"
    elif moeda == 1:
        return "coroa"
# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Fizemos login como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.channel.send(f"Hello! I am {bot.user}")
@bot.command()
async def bye(ctx):
    await ctx.channel.send("\U0001f642")
@bot.command()
async def senha(ctx):
    await ctx.channel.send(gen_pass(10))
@bot.command()
async def moeda(ctx):    
    await ctx.channel.send(caraoucoroa())
@bot.command()
async def comandos(ctx):
    await ctx.channel.send("'$hello': olá" )
    await ctx.channel.send("'$bye': tchau")
    await ctx.channel.send("'$senha': gerar senha aleatoria")
    await ctx.channel.send("'$moeda': jogar cara ou coroa")
    await ctx.channel.send("'$comandos': mostrar comandos")
    await ctx.channel.send("'$joined + usuario' : mostrar quando o usuario entrou")
@bot.command()
async def joined(ctx, *, member: discord.Member):
    await ctx.send(f'{member} joined on {member.joined_at}')
bot.ru("")
