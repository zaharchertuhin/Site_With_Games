from django.urls import path
import django.contrib.auth.views as auth_views
from accounts.views import UserCreationView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('signup/', UserCreationView.as_view(), name="sign_up"),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name="password_change"),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm")
]