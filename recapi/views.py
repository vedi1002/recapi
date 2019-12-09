from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from recapi.models import ProductRecs
import json
from rest_framework import status

# Create your views here.
class ListProducts(APIView):


    def get(self,request):
        data = json.loads(request.body.decode('utf-8'))
        thisRecs = ProductRecs.objects.get(userId=data['userid'])
        prodList = [thisRecs.prod1,
                    thisRecs.prod2,
                    thisRecs.prod3,
                    thisRecs.prod4,
                    thisRecs.prod5,
                    thisRecs.prod6,
                    thisRecs.prod7,
                    thisRecs.prod8,
                    thisRecs.prod9,
                    thisRecs.prod10]
        responseDict = {'prods':prodList}
        return Response(responseDict)

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        pr = ProductRecs.objects.create(userId=data['userid'],
                         prod1=data['prod1'],
                         prod2=data['prod2'],
                         prod3=data['prod3'],
                         prod4=data['prod4'],
                         prod5=data['prod5'],
                         prod6=data['prod6'],
                         prod7=data['prod7'],
                         prod8=data['prod8'],
                         prod9=data['prod9'],
                         prod10=data['prod10'])
        return Response(status=status.HTTP_201_CREATED)