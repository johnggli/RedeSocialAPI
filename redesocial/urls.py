from django.urls import path
from .views import *

urlpatterns = [
    path('import/', ImportJson.as_view()),
    path('profiles/', ProfileView.as_view())
]