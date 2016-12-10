from django.http import JsonResponse

from websocket.sender import send_command


def swipe_left(request):
    send_command("swipe_left", {})
    return JsonResponse({"result": "ok"})


def swipe_right(request):
    send_command("swipe_right", {})
    return JsonResponse({"result": "ok"})
