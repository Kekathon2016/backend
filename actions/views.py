from django.http import JsonResponse

from websocket.sender import send_command, send_status


def swipe_left(request):
    send_command("swipe", {"direction": "left"})
    return JsonResponse({"result": "ok"})


def swipe_right(request):
    send_command("swipe", {"direction": "right"})
    return JsonResponse({"result": "ok"})


def show(request):
    print("show")
    send_command("visible", True)
    send_status()
    return JsonResponse({"result": "ok"})


def hide(request):
    print("hide")
    send_command("visible", False)
    return JsonResponse({"result": "ok"})


def show_table(request):
    send_command("show_table", True)
    return JsonResponse({"result": "ok"})


def hide_table(request):
    send_command("show_table", False)
    return JsonResponse({"result": "ok"})
