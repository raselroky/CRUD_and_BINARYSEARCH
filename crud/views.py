from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,ListAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView,UpdateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView
from .serializers import NewsSerializer,AddressSerializer
from .models import News,Address
from rest_framework.filters import SearchFilter


class NewsListCreateAPIView(ListCreateAPIView):
    queryset=News.objects.all()
    serializer_class=NewsSerializer

class NewsListAPIView(ListAPIView):
    queryset=News.objects.all()
    serializer_class=NewsSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name','email', 'rating']

class NewsRetrieveAPIView(RetrieveAPIView):
    queryset=News.objects.all()
    serializer_class=NewsSerializer
    lookup_field='id'

class NewsUpdateAPIView(RetrieveUpdateAPIView):
    queryset=News.objects.all()
    serializer_class=NewsSerializer
    lookup_field='id'
    
class NewsDestroyAPIView(RetrieveDestroyAPIView):
    queryset=News.objects.all()
    serializer_class=NewsSerializer
    lookup_field='id'