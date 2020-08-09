import discord

import config
import fileManager
import guildManager

#Put functions here that should be run when a new user joins server (like give roles or something), the onboard() function should contain all of them and that is what you should call
async def onboard(client, user, channel):
    await give_starter_role(client, channel, user)

async def give_starter_role(client, channel, user):
    role = guildManager.get_default_role_from_config(channel, client.guilds)
    await user.add_roles(role)