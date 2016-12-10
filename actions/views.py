from django.http import JsonResponse

from websocket.sender import send_command, send_status


def swipe_left(request):
    send_command("swipe", {"direction": "left("})
    return JsonResponse({"result": "ok"})


def swipe_right(request):
    send_command("swipe", {"direction": "right"})
    return JsonResponse({"result": "ok"})


def show(request):
    send_command("visible", True)
    send_status()
    return JsonResponse({"result": "ok"})


def hide(request):
    send_command("visible", False)
    return JsonResponse({"result": "ok"})
