from django.urls import path
from .views import leadList, leadDetail, leadCreate

app_name = "leads"

urlpatterns = [
    path('', leadList),
    path('<int:pk>/', leadDetail),
    path('create/', leadCreate)
]