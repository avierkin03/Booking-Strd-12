from django.shortcuts import render
from .models import Category, Room, Booking

# функція представлення головної сторінки зі списком кімнат
def rooms_list(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms
    }
    return render(request, template_name="main_page.html", context=context)


# функція представлення сторінки з детальним описом кімнати
def room_detail(request, room_id):
    room = Room.objects.get(id = room_id)
    context = {
        "room": room
    }
    return render(request, template_name="room_detail.html", context=context)