# arduino_control/urls.py
from django.contrib import admin
from django.urls import path
from connect_arduino.views import control_page, send_signal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', control_page, name='control_page'),
    path('send_signal/', send_signal, name='send_signal'),
]
