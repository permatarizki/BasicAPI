from rest_framework import serializers
from resepmakanan import models

class MakananSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Makanan
        fields = '__all__'

class BahanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bahan
        fields = '__all__'