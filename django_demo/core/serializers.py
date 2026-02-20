from rest_framework import serializers    #import serializers tool
from .models import Product   #importing product model 
class ProductSerializer(serializers.ModelSerializer):   #create serializer for product model/class/table
    class Meta:
        model = Product         #tell serializer which model to convert 
        fields = '__all__'      #include all model/class table fields
