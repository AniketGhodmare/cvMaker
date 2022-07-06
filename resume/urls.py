from django.urls import path
from resume.views import *

urlpatterns = [
    path('',index),
    path('create/',create),
]