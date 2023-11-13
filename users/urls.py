from django.urls import path
from users.api.views import ListUsers
from users.api.views import UserRegistrationView, UserLoginView

urlpatterns = [
    path('users-list/', ListUsers.as_view(), name='users-list'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login')
]
