# control_app/views.py
from django.shortcuts import render
from django.http import HttpResponse
import serial

def control_page(request):
    return render(request, 'connect_arduino/connect_arduino.html')

def send_signal(request):
    ser = serial.Serial('COM3', 9600)  # 포트 및 속도를 Arduino에 맞게 설정

    signal = request.GET.get('signal', '')
    ser.write(signal.encode())  # 문자열을 바이트로 변환하여 Arduino로 전송

    ser.close()
    return HttpResponse(f"Signal {signal} sent to Arduino")
