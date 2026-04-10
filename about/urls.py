from django.urls import path
from .views import AboutInfoView, SkillListView, AboutCreateView, SkillCreateView, AboutUpdateView, SkillUpdateView

urlpatterns = [
    path('about/', AboutCreateView.as_view(), name='about'),
    path('info/', AboutInfoView.as_view(), name='info'),
    path('update_about/<int:id>/', AboutUpdateView.as_view(), name='update_about'),
    path('create_skills/', SkillCreateView.as_view(), name='create_skills'),
    path('skills/', SkillListView.as_view(), name='skills'),
    path('update_skill/<int:id>/', SkillUpdateView.as_view(), name='update_skill'),
]