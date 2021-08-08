from django.urls import path
from .views import leadList, leadDetail, leadCreate, leadUpdate, leadDelete

app_name = "leads"

urlpatterns = [
    path('', leadList),
    path('<int:pk>/', leadDetail),
    path('create/', leadCreate),
    path('<int:pk>/update', leadUpdate),
    path('<int:pk>/delete', leadDelete),
]