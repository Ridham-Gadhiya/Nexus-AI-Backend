from django.urls import path
from .views import DeveloperListView, DeveloperCreateView, DeveloperUpdateView, DeveloperDeleteView

urlpatterns = [
    path('create_developers/', DeveloperCreateView.as_view(), name='list_developers'),
    path('list_developers/', DeveloperListView.as_view(), name='list_developers'),
    path('update_developers/', DeveloperUpdateView.as_view(), name='list_developers'),
    path('delete_developers/', DeveloperDeleteView.as_view(), name='list_developers'),
]