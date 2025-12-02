from django.shortcuts import render
import datetime

def home(request):
    context = {
        "message": "Welcome to my Module 5 Django Tutorial!",
        "time": datetime.datetime.now()
    }
    return render(request, "main/home.html", context)
