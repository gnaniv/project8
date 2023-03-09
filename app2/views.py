from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def keerthi(request):
    return HttpResponse('<h1><marquee> Keerthi suresh is anjel</marquee></<h1>')
