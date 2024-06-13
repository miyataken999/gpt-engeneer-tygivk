from django.urls import path
from . import views

urlpatterns = [
    path('shops/', views.ShopView.as_view()),
]