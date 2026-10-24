from django.urls import path
from booking import views

urlpatterns = [
    path("", views.rooms_list, name="main"),
    path("/room/<int:room_id>", views.room_detail, name="room_detail"),
]