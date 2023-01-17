from django.core.exceptions import ObjectDoesNotExist
from users.models import Customer, Activities
from bid.models import Bid, CustomerBid
from matches.models import Match
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from api.serializers import (CustomerSerializer, 
                            CustomerSettingsSerializer,
                            CustomerBidSerializer,
                            BidSerializer, 
                            MatchSerializer, 
                            ActivitiesSerializer
                            )


class CustomerRegisterAPIView(CreateAPIView):
    serializer_class = CustomerSerializer


class CustomerSettingsAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomerSettingsSerializer
    queryset = Customer.objects.all()


class ListBidAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BidSerializer
    queryset = Bid.objects.all()


class CreateBidAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomerBidSerializer


class ListCreatedBidAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomerBidSerializer
    
    def get_queryset(self):
        return CustomerBid.objects.filter(customer=self.kwargs["pk"])


class RetrieveMatchDescriptionAPIView(RetrieveAPIView):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()


class ActivitiesAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ActivitiesSerializer

    def get_queryset(self):
        return Activities.objects.filter(customer=self.kwargs["pk"])


class BidResultAPIView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            customer_id = kwargs.get("customer_id", None)
            bid_id = kwargs.get("bid_id", None)
            if customer_id is None or bid_id is None:
                return Response(
                        {
                            "message": "Please provide valid customer and bid id"
                        }, status=status.HTTP_404_NOT_FOUND)
            customer_bid = CustomerBid.objects.get(customer=customer_id, bid=bid_id)
            bid_result = customer_bid.calculate_money_obtained_from_bid()
            return Response(
                        {
                            "match_result": customer_bid.bid.match.match_result,
                            "money": bid_result
                        }, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(
                {
                    "message": "Customer or bid with given id does not exist"
                }, status=status.HTTP_404_NOT_FOUND)
