import discord
import os
from discord.ext import commands
from drive_service import find_image

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='k!', intents=intents)


@bot.command()
async def mot(ctx, *, mot: str):
  url = find_image(mot)
  if url:
    await ctx.send(file=discord.File(
        await ctx.bot.http._HTTPClient__session.get(url).content))
  else:
    await ctx.send(f"Aucune image trouvée pour **{mot}**.")


bot.run(os.environ['TOKEN_BOT_DS'])
