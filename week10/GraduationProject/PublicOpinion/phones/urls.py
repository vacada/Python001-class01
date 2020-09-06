from django.urls import path
from . import views

urlpatterns = [
    path('index/<int:rank>', views.phone_comment),
    path('ranks', views.phone_rank),
]