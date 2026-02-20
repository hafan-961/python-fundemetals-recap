from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer



class ProductList(APIView):
    def get(self,request):
        #fetch all the rows from postgres
        products = Product.objects.all()
        #convert db to json fromat
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
def add_product(request):
    return render(request, "add_product.html")




# Create your views here.
