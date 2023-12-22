from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (UserRegistrationView,UserLoginView)
from django.urls import path

urlpatterns = [
    path('registration/', UserRegistrationView.as_view()),
    path('login/',UserLoginView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]