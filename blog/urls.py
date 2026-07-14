from django.urls import path
from .views import APIListPost,APIDestroyPost,APIDetailPost,APIUpdatePost,APICreatePost

urlpatterns = [
    path("", APIListPost.as_view()),
    path("get/<int:pk>/", APIDetailPost.as_view()),
    path("put/<int:pk>/", APIUpdatePost.as_view()),
    path("delete/<int:pk>/", APIDestroyPost.as_view()),
    path("post/", APICreatePost.as_view()),
]
