from django.urls import path
from .views import leadList, leadDetail, leadCreate, leadUpdate, leadDelete

app_name = "leads"

urlpatterns = [
    path('', leadList, name='lead-list'),
    path('<int:pk>/', leadDetail, name='lead-detail'),
    path('create/', leadCreate, name='lead-create'),
    path('<int:pk>/update', leadUpdate, name='lead-update'),
    path('<int:pk>/delete', leadDelete, name='lead-delete'),
]