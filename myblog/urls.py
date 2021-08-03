from django.urls import path
from .views import Main, Detail

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('post/<int:pk>', Detail.as_view(), name='detail'),
]
