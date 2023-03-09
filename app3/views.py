from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def anju(request):
    return HttpResponse('Anjali oka kovvu fellow')