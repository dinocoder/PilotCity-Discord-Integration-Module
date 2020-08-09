import discord
import config
import fileManager

async def create_tracked_invite(channel, studentID):
    #Create invite (max uses should be 2, not 50 but should only ever be used once)
    invite = await channel.create_invite(max_uses = 50)

    #Read json file for student database (replace with commands to read a mongo database rather than json)
    students_json = fileManager.readJson(config.STUDENT_DATABASE_PATH)
    #Link the discord INVITE to the student, to be read when they join with their Discord account
    students_json[studentID]["discordInvite"] = invite.id
    #Update the student database file (replace with commands to read a mongo database rather than json)
    fileManager.dumpJson(config.STUDENT_DATABASE_PATH, students_json)

    #Update invite state
    await update_invite_state(channel)

    await channel.send("student " + studentID + " has been linked to invite " + invite.url + ", waiting for their discord account to join")
    return invite

async def find_recently_changed_invite(channel, new_invite_state):
    #Load old invite state from Pickle file (using the Dill module otherwise we will get anerror about weakref objects)
    old_invite_state = fileManager.pickleLoad_dill(config.INVITE_STATES_FOLDER / (str(channel.id) + ".pkl"))

    #Iterate through all invites and compare their IDs and uses
    for i in new_invite_state:
        for j in old_invite_state:
            #If two invites share and ID and the NEW uses are greater than the OLD uses, this indicates that the user used this invite. Return it.
            if i['id'] == j['id'] and i['uses'] > j['uses']:
                return i['id']

#State management
async def get_invite_state(channel):
    #Get all invites for a channel
    invites = await channel.invites()
    #Change properties of the invite class that cause problems with pickling to simpler forms
    for i in invites:
        i.channel = i.channel.id
        i.inviter = i.inviter.id
    #Turn list of INVITE objects to a list of DICT objects, only keeping the important attributes specified in config
    invite_list = [dict((name, getattr(f, name)) for name in dir(f) if name in config.IMPORTANT_INVITE_ATTRS) for f in invites]
    return invite_list

async def update_invite_state(channel):
    #Get invite state
    invite_state = await get_invite_state(channel)
    print("UPDATING INVITE STATE")
    #Pickle the invite state DICT using the Dill module (cannot directly use pickle or there will be an error with weakref objects)
    fileManager.pickleDump_dill(config.INVITE_STATES_FOLDER / (str(channel.id) + ".pkl"), invite_state)

#async def create_invite(channel)