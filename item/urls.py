from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from item import views

urlpatterns = [
    path("", views.ItemListView.as_view(), name="list-user-items"),
    path("new", views.ItemCreateView.as_view(), name="create-item"),
]
