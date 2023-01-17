from django.urls import path
from api.jwt import EmailTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from api.views import (CustomerRegisterAPIView, 
                       CustomerSettingsAPIView,
                       ListBidAPIView,
                       CreateBidAPIView,
                       ListCreatedBidAPIView,
                       RetrieveMatchDescriptionAPIView,
                       BidResultAPIView,
                       ActivitiesAPIView)


urlpatterns = [
    path("token/", EmailTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("register/", CustomerRegisterAPIView.as_view(), name="customer_register_view"),
    path("customer/<int:pk>/settings/", CustomerSettingsAPIView.as_view(), name="customer_settings_view"),
    path("bids/", ListBidAPIView.as_view(), name="bids_list"),
    path("bid/create", CreateBidAPIView.as_view(), name="create_bid"),
    path("match/<int:pk>/description", RetrieveMatchDescriptionAPIView.as_view(), name="match_description"),
    path("customer/<int:pk>/bids", ListCreatedBidAPIView.as_view(), name="customer_created_bids"),
    path("customer/<int:customer_id>/bids/<int:bid_id>/result", BidResultAPIView.as_view(), name="bid_result"),
    path("customer/<int:pk>/activities", ActivitiesAPIView.as_view(), name="customer_activities")
]
