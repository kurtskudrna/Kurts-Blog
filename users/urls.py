from django.urls import path
from .views import RegisterationForm, UserCreationForm

urlpatterns = [
    path('register/', RegisterationForm.as_view(), name='registration-form')
]
