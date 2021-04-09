from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from item import views

urlpatterns = [
    path("", views.ItemListSellerView.as_view(), name="list-seller-items"),
    path("new", views.ItemCreateView.as_view(), name="create-item"),
    path("<str:pk>", views.ItemDetailView.as_view(), name="retrieve-item"),
    path("delete/<str:pk>", views.ItemDeleteView.as_view(), name="delete-item"),
    path(
        "<str:pk>/interest", views.InterestCreateView.as_view(), name="create-interest"
    ),
]
