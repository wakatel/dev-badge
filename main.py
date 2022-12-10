import nextcord
from nextcord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()


bot = commands.Bot()

@bot.event
async def on_ready():
    print('Logged in as ' + bot.user.name + ' (' + str(bot.user.id) + ')')

@bot.slash_command(description="Replies with pong!")
async def badge(interaction: nextcord.Interaction):
    await interaction.send("You will be able to claim your Active Developer Badge within 24 hours\n**if u don't know how to use it, LEARN CODE DUMB ASS!**\nhttps://discord.gg/4hbQQaEwPk", ephemeral=True)

bot.run(os.getenv("TOKEN"))