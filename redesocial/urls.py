from django.urls import path
from .views import *

urlpatterns = [
    path('import/', Import.as_view()),
    path('profiles/', ProfileView.as_view())
]