from django.urls import path

from .views import *

urlpatterns = [
    path('predict/', modelInterface.as_view()),
    path('correlation/', correlationMatrix.as_view())
]
