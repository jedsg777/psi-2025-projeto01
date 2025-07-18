from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('mulheres/', views.mulheres, name="mulheres"),
    path('historia/', views.historia, name="historia"),
]