# from django.shortcuts import render
# from django.http import HttpResponse
# from django.http import JsonResponse


# # Create your views here.
# def hello(request):
#     return HttpResponse("Please be silent")
# def name(request):
#     return JsonResponse({"name" : "HELLO world"})


from rest_framework.views import APIView
from rest_framework.response import Response        #send response
from.serializers import ProductSerializer       #import product from serializers
from .models import Product                 #import product from serializers file


class ProductList(APIView):
    #creating API class
    def get(self,request):
        #this method runs GET request
        products = Product.objects.all()
        #fetch all product rows form database
        serializer = ProductSerializer(products,many=True)
        #convert multiple prduct objects into json
        return Response(serializer.data)


