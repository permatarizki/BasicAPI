from django.contrib import admin
from django.urls import path, include
from resepmakanan import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'makanan', views.MakananViewSet)
router.register(r'bahan', views.BahanViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
