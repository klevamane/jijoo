from django.urls import path

from item import views

urlpatterns = [
    path("seller", views.SellerItemsListView.as_view(), name="seller-items-list"),
    path("seller/new", views.SellerItemCreateView.as_view(), name="seller-create-item"),
    path(
        "seller/delete/<str:pk>",
        views.SellerItemDeleteView.as_view(),
        name="seller-delete-item",
    ),
    path(
        "seller/<str:pk>",
        views.SellerItemDetailsView.as_view(),
        name="seller-item-details",
    ),
    path("all", views.BuyerItemsListView.as_view(), name="list-all-items"),
    path("interest", views.BuyerInterestCreateView.as_view(), name="make-interest"),
]
