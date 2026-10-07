from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework import status
# Create your views here.
class BookListCreateView(APIView):
    def get(self,request):
        books=Book.objects.all()
        serializer=BookSerializer(books,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class BookDetailView(APIView):
    def get(self,request,book_id):
        books=Book.objects.get(id=book_id)
        serializer=BookSerializer(books)
        return Response(serializer.data)
    def put(self,request,book_id):
        books=Book.objects.get(id=book_id)
        serializer=BookSerializer(books,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,book_id):
        books=Book.objects.get(id=book_id)
        serializer=BookSerializer(books,request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def delete(self,request,book_id):
        books=Book.objects.get(id=book_id)
        books.delete()
        return Response( {"message": "Book deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )

