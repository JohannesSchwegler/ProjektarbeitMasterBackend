from django.shortcuts import render
from rest_framework import viewsets
from .models import Card
from .serializers import CardSerializer
# Create your views here.

class CardView(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer