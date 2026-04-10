from django.urls import path
from .views import WorkCreateView, WorkListView, WorkDetailView, WorkUpdateView, WorkDeleteView
from . import views

urlpatterns = [
    path('create_work/', WorkCreateView.as_view(), name='create_work'),
    path('list_work/', WorkListView.as_view(), name='list_work'),
    path('detail_list_work/<int:id>/', WorkDetailView.as_view(), name='detail_list_work'),
    path('update_work/<int:id>/', WorkUpdateView.as_view(), name='update_work'),
    path('delete_work/<int:id>/', WorkDeleteView.as_view(), name='delete_work'),



]