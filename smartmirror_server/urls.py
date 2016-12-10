"""smartmirror_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from actions.views import swipe_left, swipe_right, hide, show, show_table, hide_table
from image_name.views import set_name
from websocket.views import webpage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', webpage),
    url(r'^names/set', set_name),
    url(r'^actions/swipe_left', swipe_left),
    url(r'^actions/swipe_right', swipe_right),
    url(r'^actions/show$', show),
    url(r'^actions/hide$', hide),
    url(r'^actions/show_timetable$', show_table),
    url(r'^actions/hide_timetable$', hide_table),
]
