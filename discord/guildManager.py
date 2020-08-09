import config
from discord.utils import get

def get_channel_from_id(client, id):
    #Iterate over all of the guilds that the bot is in and over all of the channels those guilds have
    return get(client.get_all_channels(), id=id)

def check_tracking_guild(guild):
    #Iterate through a guild's channels and seeing if any of their IDs match those in the database
    for i in guild.channels:
        if i.id in config.TRACKED_INVITE_CHANNELS.keys():
            return i

def get_role_from_id(guilds, id):
    all_roles = []
    for i in guilds:
        all_roles += i.roles
    return get(all_roles, id=id)

def get_default_role_from_config(channel, guilds):
    roleID = config.TRACKED_INVITE_CHANNELS[channel.id]
    return get_role_from_id(guilds, roleID)

    