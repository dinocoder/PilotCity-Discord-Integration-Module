import discord

import fileManager
import config

import inviteManager
import guildManager
import linkAccount
import onboardingProcess

#Notes:
#1. The student database used here is a JSON file, this should be changed to integrate with Mongo when added. This goes for everything here, the invite-generating commands can be replaced with requests from the app.
#2. The "fileManager.py" file is like a package thingy that I created as I found myself using these commands alot, so I turned them into a file where I can call these common simplified functions from.
#3. The "config.py" file stores the paths to all of the files here, allowing them to easily be changed when necessary. Each tracked channel must be specified in there. (more explanation in that file)
#4. The "invite_states" folder is where the live invite information of a channel is stored when it is being tracked.
#4. This program could be structured much more efficiently, functions can be split into multiple files and VERY EASILY integrated with and EXISTING Cogs standard. This will be done when integrating with the main PilotCity discord bot.
#5. In the future, this bot will need access to both recieveing requests from the platform AND reading and writing to the student database.

client = discord.Client()

#Client events start here

#Called when the client starts up
@client.event
async def on_ready():
    #Update invite states for all tracked channels when the bot starts up
    for i in config.TRACKED_INVITE_CHANNELS.keys():
        await inviteManager.update_invite_state(guildManager.get_channel_from_id(client, i))
        
    print('We have logged in as {0.user}'.format(client))

#Called when someone sends a message that the bot can see
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #Placeholder commands to simulate platform requests

    #Create invite using a Student ID, in this case passed as args from the command (this is a really really inefficient way to do this, but it's quick and will be removed when integrated with the platform)
    if message.content.startswith('$invite '):
        #Get student id from args (again this is really really inefficient)
        student_id = message.content[8:]
        print("CREATING INVITE FOR STUDENT ID: " + student_id)
        #Create tracked invite link that is linked to the Student ID through the student database
        await inviteManager.create_tracked_invite(message.channel, student_id)
    
    if message.content.startswith('$getinvites'):
        print("CURRENT ACTIVE INVITES: " + str(await message.channel.invites()))

#Called when someone joins a guild that the bot is in
@client.event
async def on_member_join(member):
    print(str(member) + ' joined ' + str(member.guild))
    #Check if we are tracking the guild for linking that the member just joined
    tracking_channel = guildManager.check_tracking_guild(member.guild)
    #The above function returns the CHANNEL object or None if we are not tracking it, so this says to run the following code if we are tracking it
    if tracking_channel:
        #Find which invite was most recently updated, showing us which one the user joined with
        #Get the current invite state to compare with the old one
        new_invite_state = await inviteManager.get_invite_state(tracking_channel)
        invite_id = await inviteManager.find_recently_changed_invite(tracking_channel, new_invite_state)
        #Link Student ID and Discord ID (the goal of this module)
        linkAccount.link_student_discord(invite_id, member)
        #Onboard the new user, do things like add special roles for tracked invites
        await onboardingProcess.onboard(client, member, tracking_channel)
    #Update the invite state as some things have changed
    await inviteManager.update_invite_state(tracking_channel)

def main():
    client.run(config.TOKEN)

if __name__ == "__main__":
    main()