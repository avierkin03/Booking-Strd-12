from django.db import models
from django.contrib.auth.models import User


# Модель "Категорія"
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# Модель "Кімната"
class Room(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField(null=True, upload_to="rooms")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="rooms")

    def __str__(self):
        return f"Room №{self.number} for {self.capacity} person(s)"


# Модель "Бронюавання"
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    start_date = models.DateField()
    end_date = models.DateField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - room №{self.room.number}"