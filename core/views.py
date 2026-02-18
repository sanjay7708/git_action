from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login,authenticate,logout
# Create your views here.

class LoginView(APIView):
    def post(self,request):
        data=request.data
        username=data.get('username')
        password=data.get('password')
        if not username or not password:
            return Response({'message':'username or password required'},status=status.HTTP_400_BAD_REQUEST)
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return Response({'message':'login successfull'},status=status.HTTP_200_OK)
        return Response({'message':'invalid credentials'},status=status.HTTP_401_UNAUTHORIZED)
    
        
