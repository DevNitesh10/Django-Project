from django.urls import path
from .views import index, about, create, contacts, partData, delete, update

urlpatterns = [
    path("",index, name="home"),
    path("about-us/",about, name="about"),
    path("create/", create, name="create"),
    path("contacts/", contacts, name="contacts"),
    path("<int:id>/", partData, name="partData"),
    path('delete/<int:id>/', delete, name='delete' ),
    path('update/<int:id>/', update, name='update' ),
]
