from rest_framework import generics, status, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission, IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken  # type: ignore
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from .models import *
from owner.serializers import OwnerRegistraionSerializer, ChangepasswordSerializer


class OwnerRegistraionView(generics.CreateAPIView):
    serializer_class = OwnerRegistraionSerializer
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "success": "Registration successful.",
                "access": str(refresh.access_token),
                "message":"Registration Successful",
            },status=status.HTTP_201_CREATED)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def owner_login(request):
    email = request.data.get('email')
    password = request.data.get('password')  
    if not email or not password:
        return Response(
            {'error': 'Email and password are required.'},
            status=status.HTTP_400_BAD_REQUEST
        )
    user = authenticate(request, email=email, password=password)
    # print("Authenticated user:", user)
    # print("Email:", email)
    # print("Password:", password)    
    if user is None:
        return Response(
            {'error': 'Invalid credentials.'},status=status.HTTP_401_UNAUTHORIZED)
    refresh = RefreshToken.for_user(user)
    return Response(
        {
            'message': 'Login successful.',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        },status=status.HTTP_200_OK)

class ChangePasswordView(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    
    def post(self, request, *args, **kwargs):
        serializer = ChangepasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            old_password = serializer.validated_data.get('old_password')
            new_password = serializer.validated_data.get('new_password')
            
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({"message":"User with this email does not exit."}, status=status.HTTP_404_NOT_FOUND)
            if not user.check_password(old_password):
                return Response({"error": "Incorrect old password."},status=status.HTTP_400_BAD_REQUEST)
            user.set_password(new_password)
            user.save()
            return Response({"message": "Password has been successfully updated."},
                            status=status.HTTP_200_OK)

# class ForgotPasswordView(APIView):
#     permission_classes = [IsAdminUser]
    
#     def post(self, request, *args, **kwargs):
#         serializer = ForgotPasswordSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data.get('email')
#             try:
#                 user = User.objects.get(email=email)
#             except User.DoesNotExist:
#                 return Response({"error": "User with this email does not exist."},status=status.HTTP_404_NOT_FOUND)
            
#             reset_link = "http://127.0.0.1:8000/api/reset_password/"
#             send_mail(
#             'Reset Your Password',
#             f'Click the link to reset your password: {reset_link}',
#             'noreply@example.com',
#             [email]
#             )
#             return Response({"message":"Mail has been sent"})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ResetPasswordView(APIView):
#     permission_classes = [AllowAny]
    
#     def post(self, request, *args, **kwargs):
#         serializer = ResetPasswordSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data.get("email")
#             try:
#                 user = User.objects.get(email=email)
#             except User.DoesNotExist:
#                 return Response({"error": "User with this email does not exist."},status=status.HTTP_404_NOT_FOUND)
            
#             password = serializer.validated_data.get("password")
#             confirm_password = serializer.validated_data.get("confirm_password")
            
#             if password != confirm_password:
#                 return Response({"message":"Password Doesn't match"}, status=status.HTTP_400_BAD_REQUEST)
#             user.set_password(password)
#             user.save()
#             return Response({"message":"Password has been changed!!!"})


        