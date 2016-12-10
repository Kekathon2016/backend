import threading
from websocket.sender import send_json


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


_already_ping = False


def pinger():
    global _already_ping
    if _already_ping:
        return
    _already_ping = True

    def ping():
        send_json({"type": "ping", "data": {}})

    set_interval(ping, 1)
