from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

class keshavcls(APIView):
    def post(self,request):
        value=request.data.get('value')
        
        return Response("Hey dude")
    
