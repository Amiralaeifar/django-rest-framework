from rest_framework.response import Response
from .serializers import UserRegisterSeralizer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import status


class UserRegister(APIView):
    
    def post(self, request):
        ser_data = UserRegisterSeralizer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_406_NOT_ACCEPTABLE)