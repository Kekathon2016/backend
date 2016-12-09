from channels import Group
from channels.sessions import channel_session

from websocket.runners import pinger


@channel_session
def ws_add(message):
    Group("mirror").add(message.reply_channel)
    pinger()


@channel_session
def ws_msg(message):
    print(message.content['text'])


@channel_session
def ws_disconnect(message):
    Group("mirror").discard(message.reply_channel)
