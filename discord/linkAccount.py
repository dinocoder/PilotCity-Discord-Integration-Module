import config
import fileManager

def link_student_discord(invite_id, user):
    #Read the student database (replace with commands to read a mongo database rather than json)
    student_database = fileManager.readJson(config.STUDENT_DATABASE_PATH)
    #Iterate over each student, if they find the student that should have used the invite that we are checking, assign their Discord ID, username, and discriminator the the student
    for i in student_database.values():
        if i['discordInvite'] == invite_id:
            i['discordID'] = user.id
            i['currentDiscordUsername'] = user.name
            i['currentDiscordDiscrim'] = user.discriminator
            break
    #Update the student database (replace with commands to read a mongo database rather than json)
    fileManager.dumpJson(config.STUDENT_DATABASE_PATH, student_database)