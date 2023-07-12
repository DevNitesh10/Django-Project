from django.urls import path
from .views import index
from .views import about

urlpatterns = [
    path("",index),
    path("about-us",about)
]
