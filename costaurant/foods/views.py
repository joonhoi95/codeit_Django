from typing import ContextManager
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    today = datetime.today().date()
    context1 = {"date":today}
    return render(request, 'foods/index.html', context=context1)


def chicken(request):
    return render(request, 'foods/chicken.html')