from rest_framework import viewsets, permissions
from .serializers import DishSerializer
from .models import Dish

class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DishSerializer