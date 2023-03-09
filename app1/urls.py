from app1.views import *

from django.urls import path

app_name='real hero'

urlpatterns=[
    path('PSPK/',PSPK,name='PSPK')
]