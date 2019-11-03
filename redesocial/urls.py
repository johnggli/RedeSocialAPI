from django.urls import path
from .views import *

urlpatterns = [
    path('import/', ImportJson.as_view()),
    path('profiles/', ProfileList.as_view()),
    path('profiles/<int:pk>', ProfileDetail.as_view())
]