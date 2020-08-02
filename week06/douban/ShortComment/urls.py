from django.urls import path
from . import views


urlpatterns = [
    path('index', views.book_short),
    path('table', views.short_tables),
]
