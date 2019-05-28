from django.db import models

# Create your models here.

class Dish(models.Model):
    FOOD_TYPES = [
    ('DES', 'Dessert'),
    ('ENT', 'Entry'),
    ('SOP', 'Soup')
    ]
    name = models.CharField(max_length=100)
    dish_type = models.CharField(max_length=3,choices=FOOD_TYPES)


