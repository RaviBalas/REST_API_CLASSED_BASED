from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EmployeeModel
from .serilizers import EmployeeSerializer
from django.http import Http404
class EmployeeView(APIView):
    def get(self,request):
        obj=EmployeeModel.objects.all()
        serializer=EmployeeSerializer(obj,many=True)
        return Response(serializer.data, status=200)
    def post(self,request):
        serilizer=EmployeeSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status=201)
        return Response(serilizer.errors, status=400) # if error
            
class EmplyeeViewId(APIView):
    def get_object(self,id):
        try:
            return EmployeeModel.objects.get(pk=id)
        except EmployeeModel.DoesNotExist as e :
            raise   Http404  # Response({"error": "Not found."},status=404)
    def get(self,request,id=None):
        instance = self.get_object(id)
        serilizer=EmployeeSerializer(instance)
        return Response(serilizer.data)
        
    def put(self,request,id=None):
        serializer=EmployeeSerializer(self.get_object(id),request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors,status=400)
    def delete(self,request,id=None):
        instance = self.get_object(id)
        serilizer=EmployeeSerializer(instance)
        instance.delete()
        return Response(serilizer.data)
        