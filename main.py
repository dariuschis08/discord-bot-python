import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("MTU0MzI4MjI4NjQyODk0NjUyMw.GPFklj.zbq1WWe-ZDg1I5IqFJXYKJGPIf2FPCjCipD0_4")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
  print(f"Logged in as {bot.user.name} - {bot.user.id}")


@bot.event
async def on_member_join(member):
  role_name = "Membru"
  role = discord.utils.get(member.guild.roles, name=role_name)

  if role:
    await member.add_roles(role)
    print(f"Rolul {role_name} a fost acordat lui {member.name}.")
  else:
    print(f"Rolul '{role_name}' nu a fost găsit pe server!")


@bot.command()
async def salut(ctx):
  await ctx.send(f"Salut, {ctx.author.name}!")


bot.run(MTU0MzI4MjI4NjQyODk0NjUyMw.GPFklj.zbq1WWe-ZDg1I5IqFJXYKJGPIf2FPCjCipD0_4)