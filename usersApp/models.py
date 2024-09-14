from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import AbstractUser


class University(models.Model):
    name = models.CharField(max_length=128, unique=True)


class User(AbstractUser):
    STATUS_CHOICES = (
        ('A', 'admin'),
        ('U', 'user'),
    )
    status =  models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')
    university_id = models.ForeignKey(University, on_delete=models.CASCADE, to_field="id", null=True)


class Institutes(models.Model):
    institutes_name = models.CharField(max_length=128)
    university_id = models.ForeignKey(University ,on_delete=models.CASCADE, to_field='id')


class PC(models.Model):
    STATUS_CHOICES = (
        ('W', 'Працює'),
        ('DW', 'Не працює'),
        ('R', 'На ремонті'),
    )
    university_id = models.ForeignKey(University ,on_delete=models.CASCADE, to_field='id')
    institutes_id = models.ForeignKey(Institutes, on_delete=models.SET_NULL, to_field="id", null=True)
    model = models.CharField(max_length=128)
    inventory_number = models.IntegerField(unique=True)
    dateOfPurchase = models.DateField(default=date.today)
    processor = models.CharField(max_length=128)
    RAM = models.IntegerField(default=0)
    video_core = models.CharField(max_length=128)
    office = models.CharField(max_length=10)
    corps = models.IntegerField(default=0)
    image = models.ImageField(upload_to='pc_images/', blank=True, default='pc_images/none.png')
    os = models.CharField(max_length=50)
    description = models.TextField()
    memory = models.IntegerField(default=0)
    status =  models.CharField(max_length=2, choices=STATUS_CHOICES, default='W')


    def formatted_date(self):
        return self.dateOfPurchase.strftime('%d.%m.%Y')
    

