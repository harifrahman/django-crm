from django.urls import path
from .views import homePage

app_name = "leads"

urlpatterns = [
    path('all/', homePage)
]