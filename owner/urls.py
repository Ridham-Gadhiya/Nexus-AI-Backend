from django.urls import path
from .views import OwnerRegistraionView, ChangePasswordView
from . import views

urlpatterns = [
    path('owner_registration/', OwnerRegistraionView.as_view(), name='owner_registration'),
    path('owner_login/', views.owner_login, name='owner_login'),
    path('change_pass/', ChangePasswordView.as_view(), name='change_pass'),
    # path('forgot_pass/', ForgotPasswordView.as_view(), name='forgot_pass'),
    # path('reset_pass/', ResetPasswordView.as_view(), name='reset_pass'),


]