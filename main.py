import discord
from discord.ext import commands
from utilities.common import config
import glob

if __name__ == '__main__':

    # Set the command prefix here
    bot = commands.Bot(command_prefix=config(['prefix']))

    # Load extensions from files
    for filename in glob.iglob('.\\cogs\\*'):
        if filename.split('.')[-1] == 'py' and filename.split('\\')[-1][0] is not '_':
            print('Loading extension ' + filename.split('.')[1].split('\\')[-1] + '...')
            bot.load_extension('cogs.' + filename.split('.')[1].split('\\')[-1])



    # CALLBACK SETUP

    @bot.event
    async def on_ready():
        print(f'Logged in as: {bot.user.name} - {bot.user.id} - Version: {discord.__version__}')
        await bot.change_presence(activity=discord.Game(name='Testing Python 🐍'))
        print(f'Successfully logged in and booted...!')

    @bot.event
    async def on_message(message):
        ctx = await bot.get_context(message)
        await bot.invoke(ctx)
        #print(str(message.author.id) + ': ' + message.content)
        pass

    @bot.event
    async def on_raw_reaction_add(payload):
        #print(str(payload.user_id) + ' ' + str(payload.emoji) + '  ' + ('Unicode 😠' if payload.emoji.is_unicode_emoji() else 'Not Unicode 😠'))
        pass

    @bot.event
    async def on_raw_message_edit(payload):
        #print(str(payload.cached_message.author.id) + ': ' + payload.cached_message.content)
        pass


    # Run bot
    print("Logging in...")
    bot.run(config(['Discord', 'token'], filename='tokens.toml'))