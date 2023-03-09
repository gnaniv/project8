from app2.views import *
from django.urls import path

app_name='anjel'

urlpatterns=[
    path('keerthi/',keerthi,name='keerthi')
]