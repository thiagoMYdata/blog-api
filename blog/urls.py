from django.urls import path
from .views import APIListPost

urlpatterns = [
    path("", APIListPost.as_view()),
]
