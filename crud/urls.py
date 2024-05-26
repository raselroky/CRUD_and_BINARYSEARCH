from django.contrib import admin
from django.urls import path
from .views import NewsListCreateAPIView,NewsListAPIView,NewsUpdateAPIView,NewsRetrieveAPIView,NewsDestroyAPIView
urlpatterns = [
    path('news-create/',NewsListCreateAPIView.as_view(),name='news-create-api'),
    path('news-list/',NewsListAPIView.as_view(),name='news-all-list-api'),
    path('news-retrieve/<int:id>',NewsRetrieveAPIView.as_view(),name='news-retrieve-api'),
    path('news-update/<int:id>',NewsUpdateAPIView.as_view(),name='news-update-api'),
    path('news-destroy/<int:id>',NewsDestroyAPIView.as_view(),name='news-destroy-api'),
]
