from django.urls import path
from .views import (
    leadList, leadDetail, leadCreate, leadUpdate, leadDelete,
    LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView
    )

app_name = "leads"

urlpatterns = [
    # using function view
    # path('', leadList, name='lead-list'),
    # path('<int:pk>/', leadDetail, name='lead-detail'),
    # path('create/', leadCreate, name='lead-create'),
    # path('<int:pk>/update', leadUpdate, name='lead-update'),
    # path('<int:pk>/delete', leadDelete, name='lead-delete'),
    

    # using class based template views
    path('', LeadListView.as_view(), name='lead-list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
    path('<int:pk>/update', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete', LeadDeleteView.as_view(), name='lead-delete'),
]