from django.shortcuts import render
from .models import Category, Room, Booking

# функція представлення головної сторінки зі списком кімнат
def rooms_list(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms
    }

    if request.method == "POST":
        # Отримуємо дані з POST-запиту
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        capacity = request.POST.get("capacity")
        price_from = request.POST.get("price_from")
        price_to = request.POST.get("price_to")
        # Застосовуємо фільтри для списку кімнат
        rooms = rooms.exclude(bookings__start_date__lt=end_date, bookings__end_date__gt=start_date)
        if capacity:
            rooms = rooms.filter(capacity__gte=int(capacity))
        if price_from:
            rooms = rooms.filter(price__gte=float(price_from))
        if price_to:
            rooms = rooms.filter(price__lte=float(price_to))
        # Оновлюємо контекст із введеними даними
        context.update({
            "rooms": rooms,
            "start_date": start_date,
            "end_date": end_date,
            "capacity": capacity,
            "price_from": price_from,
            "price_to": price_to
        })

    return render(request, template_name="main_page.html", context=context)


# функція представлення сторінки з детальним описом кімнати
def room_detail(request, room_id):
    room = Room.objects.get(id = room_id)
    context = {
        "room": room
    }
    return render(request, template_name="room_detail.html", context=context)