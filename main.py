import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot connecté en tant que {bot.user}")

# Sync les commandes slash
@bot.event
async def setup_hook():
    await bot.tree.sync()

# Slash command /roll
@bot.tree.command(name="roll", description="Lance un dé à 6 faces")
async def roll(interaction: discord.Interaction):
    import random
    result = random.randint(1, 6)
    await interaction.response.send_message(f"🎲 Tu as lancé un dé : **{result}**")

bot.run(TOKEN)
