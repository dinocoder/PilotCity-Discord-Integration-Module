
#IGNORE THIS FILE IT DOESN'T WORK AND I AM GOING TO DO THIS A DIFFERENT WAY





import flask
from quart import Quart
from twisted.internet.defer import inlineCallbacks, returnValue
import asyncio

import inviteManager
import guildManager

app = Quart(__name__)
#app.config['DEBUG'] = True

client = None

#Link the path '/' to the function home() and let it be accessible through GET requests
@app.route('/api/v1/resources/createinvite', methods=['GET'])
async def api_createinvite():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        studentID = request.args['id']
    else:
        return ("Error: No id field provided. Please specify an id.")
    if 'channel' in request.args:
        channelID = request.args['channel']
    else:
        return ("Error. No channel field provided. Please specify a channel id.")
    
    channel = guildManager.get_channel_from_id(client, channelID)
    return await inviteManager.create_tracked_invite(channel, studentID).link

async def main(discordClient, loop):
    client = discordClient
    print("running api")
    print(client)
    await app.run()