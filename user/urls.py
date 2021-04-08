from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from user import views

urlpatterns = [
    # profile
    path("create", views.CreateUser.as_view(), name="signup"),
]
