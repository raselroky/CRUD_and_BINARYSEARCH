from django.contrib import admin
from django.urls import path
from .views import SearchAPIView
urlpatterns = [
    path('search-data/',SearchAPIView.as_view(),name='news-data-search-api-use-binary-search'),
    
]
