import discord
from discord.ext import commands
import os

#import all of the cogs
from help_cog import help_cog
from music_cog import music_cog

bot = commands.Bot(command_prefix='/')

#remove the default help command so that we can write out own
bot.remove_command('help')

#register the class with the bot
bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))

# bắt đầu bot bằng mã thông báo của chúng tôi
bot . run ( bộ điều khiển getenv               ( "MTAwMDkxNjQwMTU5NjM5OTcyNw.GEanQ6.j4oXZ5ObzDPcSndzvHbBT4F0xVc2gr_Twt6OEY" )
