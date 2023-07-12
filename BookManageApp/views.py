from django.shortcuts import render

from .serializers import Bookserializer
from .models import CustomUser,Book
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.
class BookList(generics.ListAPIView):
    queryset=Book.objects.all()
    serializer_class=Bookserializer

class BookCreate(generics.CreateAPIView):
    queryset=Book.objects.all()
    serializer_class=Bookserializer
    permission_classes=[IsAuthenticated]

    def post(self, request, *args, **kwargs):
        response= super().post(request, *args, **kwargs)
        return Response({'message':'Book added'})

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    

class BookEdit(generics.RetrieveUpdateDestroyAPIView):
     queryset=Book.objects.all()
     serializer_class=Bookserializer
     permission_classes=[IsAuthenticated]

     def patch(self, request, *args, **kwargs):
        instance=self.get_object()
        if instance.author != request.user:
           return Response({ 'error':"the user do not have the permission to edit the book"})
        return super().patch(request, *args, **kwargs)
     
     def put(self, request, *args, **kwargs):
        instance=self.get_object()
        if instance.author != request.user:
           return Response({ 'error':"the user do not have the permission to edit the book"})
        return super().put(request, *args, **kwargs)
     
     def delete(self, request, *args, **kwargs):
        instance=self.get_object()
        if instance.author != request.user:
           return Response({ 'error':"the user do not have the permission to delete the book"})
        
        response= super().delete(request, *args, **kwargs)
        return Response({'message':'Book deleted'})
    