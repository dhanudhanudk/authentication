
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.urls import reverse_lazy
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response 
from rest_framework.views import APIView 
from rest_framework.views import status 
from.serializers import* 
from django.http import Http404
from rest_framework.authtoken.models import Token
from.authentication import APIKeyAuthentication
  
# Basic Auth
  
class SampleViews(APIView):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated]   
    def get(self,request):
        serializers=SampleData.objects.all()
        serializer=SampleSerializer(serializers,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer= SampleSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response({"msg":"very good", 'data':serializer.data},status=status.HTTP_201_CREATED)
        
        return Response({"status": "error",'data':serializer.data},status=status.HTTP_404_NOT_FOUND)
        
class SampleEdit(APIView):

    def get_object(self,id):
        try:
            return SampleData.objects.get(id=id)
        except SampleData.DoesNotExist:
            return Http404
        
    def get(self,request,id):
        serializers= self.get_object(id=id)
        serializer=SampleSerializer(serializers)
        return Response(serializer.data)  
        
    def put(self, request,id):
        serializers=SampleData.objects.get(id=id)
        serializer=SampleSerializer(serializers,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"successfully update","data":serializer.data},status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_302_FOUND)
        
    def delete(self,request,id):
         serializers=SampleData.objects.get(id=id)
         serializers.delete()
         return Response({"delete"},status=status.HTTP_201_CREATED)

        
# 2.token auth

class RegisterToken(APIView): 

    def get(self,request):
        serializers=SampleData.objects.all()
        serializer=SampleSerializer(serializers,many=True)
        return Response(serializer.data)
    
  
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user=User.objects.get(username = serializer.data['username'],
                                  password = serializer.data['password'])
            token_obj,_=Token.objects.get_or_create(user=user)
            return Response({'data': serializer.data,'token':str(token_obj)},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.data.get("old_password")
            new_password = serializer.data.get("new_password")

            if not check_password(old_password, user.password):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            new_password = serializer.validated_data['new_password']
            user.set_password(new_password)
            user.save()

        return Response({"message": "Password updated successfully."}, status=status.HTTP_200_OK)
        
class LoginUser(APIView):

    def post(self,request):
        data=request.data
        user= User.objects.filter(username=data['username'],
                                                password = data['password']).first()
        if user is None:
            return Response({"msg":"username and password not exist , try agin",})
        
        return Response({"msg":" login success","success":True,})
    
class Logout(APIView):
    def post(self, request, format=None):
        request.user.auth_token.delete()
        return Response('User Logged out successfully')
    
# Bearer authen.

from rest_framework_simplejwt.tokens import RefreshToken
  
# class RegisterBearerToken(APIView):
    

#     def get(self,request):
#         serializers=SampleData.objects.all()
#         serializer=SampleSerializer(serializers,many=True)
#         return Response(serializer.data)
    
  
#     def post(self,request):
#         serializer=UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
            
#             return Response({'data': serializer.data,},status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
# class Login(APIView):
#     def post(self,request):
#         data=request.data
#         user= User.objects.filter(username=data['username'],
#                                                 password = data['password']).first()
#         if user is None:
#             return Response({"msg":"username and password not exist , try agin",})
          
#         refresh = RefreshToken.for_user(user)
        
#         return Response({"msg":" login success","success":True,'Refresh':str(refresh),'access':str(refresh.access_token)})
    
