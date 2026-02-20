from rest_framework.decorators import  api_view
from rest_framework.response import Response
from .models import Students
from .serializers import StudentSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
# from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
@cache_page(60)         #this (60) specifies the seconds . means that data will be stored for 60 sec then it will erase
#cache = Temporary memory
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def student_list(request):

    if request.method == 'GET':
        ordering = request.query_params.get("ordering")
        search = request.query_params.get("search")     #ordering

        students = Students.objects.all()

        age = request.query_params.get("age")
        name = request.query_params.get("name")
        if age:                                         #Filter
            students = students.filter(age = age)
        if name:
            students = students.filter(name__icontains = name)  #__icontains means no charecter sensitive

        if ordering:
            students = students.order_by(ordering)        #ordering


        paginator = PageNumberPagination()
        paginator.page_size = 2         #same as settings
        paginator_students = paginator.paginate_queryset(students , request)
        serializer=StudentSerializer(paginator_students,many=True)
        return paginator.get_paginated_response(serializer.data)
        
    if request.method == 'POST':
        serializer=StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.error,status=400)
    
@cache_page(60)  
@api_view(['GET','PUT','DELETE','PATCH'])
@permission_classes([IsAuthenticated])
def student_details(request,id):
    try:
        student = Students.objects.get(id=id)
    except Students.DoesNotExist:
        return Response({'error':'Not found'},status=404)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error,status=400)
    if request.method == 'DELETE':
        student.delete()

        clear_cache() #clear the cache after deletion 
        return Response({'Student':'Deleted'})
    if request.method == 'PATCH':
        serializer = StudentSerializer(student,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error,status=400)
