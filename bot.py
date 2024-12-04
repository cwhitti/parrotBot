import discord
from secret import TOKEN

def run_discord_bot():

    # Set up bot
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client( intents=intents )

    # Set prefix
    prefix = '.'
    cmd_str = "say"

    # Show bot logged on successfully
    @client.event
    async def on_ready():

        await client.change_presence(activity=discord.Game(name="Try .say"))
        print(f'{client.user} is now running!')

    # Message Handler
    @client.event
    async def on_message(msg):

        # Don't listen to self
        if msg.author == client.user or msg.attachments:
            return 0 # skip

        # Grab the Message Content
        content = msg.content

        # Check if the message starts with a known command
        if content.startswith(prefix + cmd_str):

            to_say = content.strip( f"{prefix + cmd_str}")

            # Send hello back
            await msg.channel.send(f"{to_say}")

    # Run Bot with Token
        # Should be  the very last command inside of run_discord_bot 
    client.run( TOKEN )
