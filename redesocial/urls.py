from django.urls import path
from .views import *

urlpatterns = [
    path('import/', ImportJson.as_view()),
    path('profiles/', ProfileList.as_view(), name=ProfileList.name),
    path('profiles/<int:pk>', ProfileDetail.as_view()),
    path('', ApiRoot.as_view()),
    path('profile-posts/', ProfilePostList.as_view(), name=ProfilePostList.name)
]