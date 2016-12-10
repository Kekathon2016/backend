import json

from image_name.models import get_name
from websocket.utils import get_dest


def send_json(obj, dest=None):
    dest = get_dest(dest)
    dest.send({'text': json.dumps(obj)})


def send_command(t, data, dest=None):
    send_json({"type": t, "data": data}, dest)


def send_name(dest=None):
    name = get_name()
    send_command("update_name", {"name": name}, dest)


def send_status(dest):
    send_name(dest)
