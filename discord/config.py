#Import path-generating module, important fro keeping folder paths consistient across platforms
from pathlib import Path

#Paths to important files and folders
STUDENT_DATABASE_PATH = "students.json"
INVITE_STATES_FOLDER = Path("invite_states/")

#Important attributes of a Discord INVITE object
IMPORTANT_INVITE_ATTRS = [
    "channel",
    "code",
    "created_at",
    "id",
    "max_age",
    "max_uses",
    "inviter",
    "revoked",
    "temporary",
    "uses"
]

#Which channels should be tracked AND what the ID of the role that should be given when they join (Select a "welcome" or "rules" channel from within the guild that you want to track and link invites for, as invites are on a by-channel basis, not a by-server basis)
TRACKED_INVITE_CHANNELS = {429105855636570124: 741005338941325474}

TOKEN = 'no hijacking pls (replace with your own bot token)'