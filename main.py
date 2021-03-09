#---Painel---
import os

os.system("cls")
os.system("title https://github.com/expurgaram")
os.system("color c")

#---CONFIG---

print(f"""
 █████╗  █████╗ ███╗  ██╗███████╗██╗ ██████╗
██╔══██╗██╔══██╗████╗ ██║██╔════╝██║██╔════╝
██║  ╚═╝██║  ██║██╔██╗██║█████╗  ██║██║  ██╗
██║  ██╗██║  ██║██║╚████║██╔══╝  ██║██║  ╚██╗
╚█████╔╝╚█████╔╝██║ ╚███║██║     ██║╚██████╔╝
 ╚════╝  ╚════╝ ╚═╝  ╚══╝╚═╝     ╚═╝ ╚═════╝""")


token = input ('\n>>> Coloque o seu token: ')
prefix = input ('>>> Coloque o prefixo que queira usar: ')

os.system("cls")
os.system("color f")

#--- BOT ---

import discord
from discord.ext import commands
import aiohttp
from time import sleep

os.system("color 6")
print("[Sueth Support] Logando na API do Discord...")

os.system("cls")
os.system("color 5")

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")

print(f'''
 ██████╗██╗   ██╗███████╗████████╗██╗  ██╗
██╔════╝██║   ██║██╔════╝╚══██╔══╝██║  ██║
╚█████╗ ██║   ██║█████╗     ██║   ███████║
 ╚═══██╗██║   ██║██╔══╝     ██║   ██╔══██║
██████╔╝╚██████╔╝███████╗   ██║   ██║  ██║
╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝''')

@bot.event
async def on_ready():
    print("\n[Sueth Support] Pronto! Estou carregando os comandos..") 
    print(f"[Sueth Support] Nick: {bot.user.name}")
    print(f"[Sueth Support] ID: {bot.user.id}\n")

os.system("color 1")
os.system("color 2")
os.system("color 3")
os.system("color 4")
os.system("color 5")
os.system("color 6")
os.system("color 7")
os.system("color 8")
os.system("color 9")
os.system("color 5")
os.system("color 1")
os.system("color 2")
os.system("color 3")
os.system("color 4")
os.system("color 5")
os.system("color 6")
os.system("color 7")
os.system("color 8")
os.system("color 9")
os.system("color 5")



@bot.event
async def on_message(message, limit: int=None):
    if message.content.startswith(prefix + 'help'):
        await message.delete()
        embedVar = discord.Embed(title=bot.user.name + " | Ajuda!", description="", color=0xff0000)
        embedVar.add_field(name=prefix + "cls", value="```Ira excluir suas mensagens!```", inline=False)
        embedVar.add_field(name=prefix + "prefix", value="```Irá mostrar o prefixo que você esta usando no selfbot!```", inline=False)
        embedVar.add_field(name=prefix + "delall", value="```Ira deletar todos os canais, e se possivel banir os membros! (precisa de permissões)```", inline=False)
        embedVar.add_field(name=prefix + "sueth", value="```Minha GitHub ```:hearts:", inline=False)
        embedVar.add_field(name="Selfbot feito por ", value="**[Sueth Fofux ^^](https://github.com/expurgaram)  **", inline=False)
        embedVar.set_thumbnail(url=message.author.avatar_url)

        await message.channel.send(embed=embedVar)
        print(f'[Sueth Completed] Comando de Help Usado!')

    if message.content.startswith(prefix + 'sueth'):
        await message.delete()
        os.system("start https://github.com/expurgaram")
        await message.channel.send("Abrindo a GitHub do Dono do SelfBot de Clear!")

    if message.content.startswith(prefix + "flood"):    
        await message.delete()
        print("[Sueth Completed] Comando de Flood Usado!")
        flood = message.content[len(prefix)+6:]
        await message.channel.send(flood)
        sleep(0.3)
        await message.channel.send(flood)
        await message.channel.send(flood)
        await message.channel.send(flood)
        await message.channel.send(flood)
        sleep(0.3)
        await message.channel.send(flood)
        await message.channel.send(flood)
        await message.channel.send(flood)
        await message.channel.send(flood)
        await message.channel.send(flood)
        sleep(0.3)
        await message.channel.send(flood)
        await message.channel.send(flood)
        await message.channel.send(flood)
        await message.channel.send(flood)
        sleep(0.3)
        await message.channel.send(flood)
        await message.channel.send(flood)
        await message.channel.send(flood)
        await message.channel.send(flood)
        sleep(0.3)
        await message.channel.send(flood)
        await message.channel.send(flood)
        await message.channel.send(flood)
        await message.channel.send(flood)
        sleep(0.3)
        await message.channel.send(flood)
        await message.channel.send(flood)
        await message.channel.send(flood)
        await message.channel.send(flood)
        await message.channel.send(flood)

    if message.content.startswith(prefix + "cls"):
        passed = 0
        failed = 0
        async for msg in message.channel.history(limit=limit):
            if msg.author.id == bot.user.id:
                try:
                    await msg.delete()
                    passed += 1
                except:
                    failed += 1
        print(f"[Sueth Completed] Removidas {passed}! foram {failed} mensagens que não pude apagar!")

    if message.content.startswith(prefix + "prefix"):
        await message.delete()
        embedw = discord.Embed(title="", description="Meu prefixo é " + prefix + " ", color=0xff0000)
        await message.channel.send(embed=embedw)
        print(f"[Sueth Completed] Comando de Prefix Usado!")

    if message.content.startswith(prefix + 'delall'):
        await message.delete()
        for member in bot.get_all_members():
            try:
                await member.ban(reason="Sueth fofux ^^", delete_message_days=5)
            except:
                continue
        for channel in message.guild.channels:
            await channel.delete()
            print(f"[Sueth Completed] Comando de Delall Usado!")

bot.run(token, bot=False)
