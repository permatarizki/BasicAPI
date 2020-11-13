from django.shortcuts import render
from rest_framework import viewsets
from resepmakanan import serializers
from resepmakanan import models

# Create your views here.
class MakananViewSet(viewsets.ModelViewSet):
    queryset = models.Makanan.objects.all()
    serializer_class = serializers.MakananSerializer

class BahanViewSet(viewsets.ModelViewSet):
    queryset = models.Bahan.objects.all()
    serializer_class = serializers.BahanSerializer