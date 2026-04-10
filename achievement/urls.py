from django.urls import path
from .views import AchievementCreateView, AchievementListView, AchievementUpdateView, WorkDeleteView

urlpatterns = [
    path('achievements/', AchievementCreateView.as_view(), name='achievements'),
    path('list_achievements/', AchievementListView.as_view(), name='list_achievements'),
    path('update_achievement/<int:id>/', AchievementUpdateView.as_view(), name='update_achievement'),
    path('delete_achievement/<int:id>/', WorkDeleteView.as_view(), name='delete_achievement'),
]