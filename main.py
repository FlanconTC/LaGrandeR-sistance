import discord
import os

TOKEN = os.getenv("DISCORD_TOKEN")
TARGET_ROLE_NAME = "Red"  # Le nom du rôle à vérifier
TRIGGER_WORD = "ping"       # Le mot déclencheur

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Connecté en tant que {client.user}")

@client.event
async def on_message(message):
    # Ignore les messages du bot lui-même
    if message.author == client.user:
        return

    # Si le mot déclencheur est dans le message
    if TRIGGER_WORD in message.content.lower():
        # Vérifie que le message vient d’un membre d’un serveur (pas en DM)
        if isinstance(message.author, discord.Member):
            # Vérifie si l’auteur a le rôle cible
            has_role = any(role.name == TARGET_ROLE_NAME for role in message.author.roles)
            if has_role:
                await message.channel.send(f"{message.author.mention} a dit '{TRIGGER_WORD}' avec le rôle {TARGET_ROLE_NAME} ✅")
            else:
                await message.channel.send(f"{message.author.mention} a dit '{TRIGGER_WORD}' mais n’a pas le rôle requis ❌")

client.run(TOKEN)
