from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from crud.models import News
from crud.serializers import NewsSerializer
from search import binary_search


class SearchAPIView(APIView):
    def post(self,request):
        email=request.data['email']
        sorted_queryset = News.objects.order_by('email')
        target_value = 'email'
        
        found_record = binary_search(sorted_queryset, target_value)
        if found_record:
            return Response({"message":"Your data is found"})
        else:
            return Response({"message":"Your data is not found"})
        
