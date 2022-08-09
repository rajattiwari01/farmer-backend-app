from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import *
from .serializers import UserSerializer, UserLoginSerializer, UserLogoutSerializer, FileUploadSerializer
import csv
from rest_framework.response import Response
from rest_framework import status
import io

class Record(generics.ListCreateAPIView):
    # get method handler
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Login(generics.GenericAPIView):
    # get method handler
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLoginSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)


class Logout(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserLogoutSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLogoutSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)



class FileUploadAPIView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        

        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data['token']
        language_code = serializer.validated_data['language_code']  
        file = serializer.validated_data['file']
        decoded_file = file.read().decode()
        # upload_products_csv.delay(decoded_file, request.user.pk)
        io_string = io.StringIO(decoded_file)
        reader = csv.reader(io_string)
        for row in reader:
            print(row)
        
        try:
            user = User.objects.get(token = token)
        except:
            user = None
        
        if not user:
            return Response({"message": "User not found"}, status=status.HTTP_400_BAD_REQUEST)
            
        UserData.objects.create(
            user = user,
            language_code = language_code,
            file = file
        )
        return Response({"message": "Success"}, status=status.HTTP_204_NO_CONTENT)

        

def index(request):
    return redirect('/api/login')