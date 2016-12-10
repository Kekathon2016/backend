from django.http import JsonResponse

from image_name.models import get_name
from image_name.models import set_name as _set_name
from websocket.sender import send_name


def set_name(request):
    name = request.GET['name']
    if name != get_name():
        _set_name(name)
        send_name()
    return JsonResponse({"result": "ok"})