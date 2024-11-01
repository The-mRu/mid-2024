from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer
from .serializers import CustomerSerializer

def home(request):
    return HttpResponse("Welcome to the Book page! (home function)")


class CustomerContactView(APIView):

    def get(self, request, *args, **kwargs):
        email = request.query_params.get('email')
        if not email:
            return Response({'error': 'Email is required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            customer = Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            return Response({'error': 'Customer not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def patch(self, request, *args, **kwargs):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required for updating.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            customer = Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            return Response({'error': 'Customer not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CustomerSerializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
