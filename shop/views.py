from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from shop.models import Shop
from shop.serializers import ShopSerializer


# Create your views here.

class ShopViewSet(viewsets.ModelViewSet):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()

# class ShopViewSet(GenericViewSet):
#     def create(self, request, *args, **kwargs):
#         serializer = ShopSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def list(self, request, *args, **kwargs):
#         queryset = Shop.objects.all()
#         return Response(ShopSerializer(queryset, many=True).data)
#
#     def update(self, request, *args, **kwargs):
#         return Response('Shop updated')
#
#     def delete(self, request, pk, *args, **kwargs):
#         shop = Shop.objects.filter(pk=pk).delete()
#         return Response('Shop deleted')
#
#     def retrieve(self, request: Request, pk, *args, **kwargs):
#         shop = Shop.objects.filter(pk=pk).first()
#
#         return Response(ShopSerializer(shop).data)
#
#     @action(methods=['POST', 'GET'], detail=True)
#     def search(self, request, pk):
#         return Response(pk)
