from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from authentication import views

urlpatterns = [
    path("signup", views.SignupView.as_view(), name="auth-signup"),
    path("login", obtain_jwt_token, name="login"),
]
