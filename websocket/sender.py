import json

from channels import Group


def send(obj):
    Group("mirror").send({'text': json.dumps(obj)})
