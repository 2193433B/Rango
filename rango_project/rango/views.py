from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'ayylmao': "Big, bold, beautiful, message!"}
    return render(request, 'rango/index.html', context=context_dict)