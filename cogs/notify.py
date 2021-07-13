from discord.ext import commands, tasks
from utilities.twitch_utils import get_stream
from utilities.common import config

class NotifyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_stream_time = ''
        self.twitch_loop.start()

    @tasks.loop(seconds=config(['Notify', 'Twitch', 'loop']))
    async def twitch_loop(self):
        stream = get_stream(config(['Notify', 'Twitch', 'streamer']))
        if stream:
            if self.last_stream_time == stream['started_at']: return
            self.last_stream_time = stream['started_at']
            channel = self.bot.get_channel(config(['Notify', 'Twitch', 'channel_id']))
            await channel.send(stream['user_name'] + ' is live! https://twitch.tv/' + config(['Notify', 'Twitch', 'streamer']) + '\n' + stream['title'])

def setup(bot): bot.add_cog(NotifyCog(bot))