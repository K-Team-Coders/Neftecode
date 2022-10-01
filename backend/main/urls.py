from django.urls import path

from .views import *

urlpatterns = [
    path('predict/', modelInterface.as_view()),
]
