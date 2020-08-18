from datetime import datetime
from django.shortcuts import render


def hello_world(request):
    our_context = {"time": datetime.now()}
    return render(request, template_name="index.html", context=our_context)
