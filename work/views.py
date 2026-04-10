from rest_framework import generics, status, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission, IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from .models import *
from work.serializers import WorkSerializer

class WorkCreateView(generics.CreateAPIView):
    serializer_class = WorkSerializer
    permission_classes = [IsAdminUser]
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        work = serializer.save()
        work.owner.add(request.user)

        print("Authenticated user:", request.user)
        print("Email:", request.user.email)

        return Response({
            'message': 'Project has been created',
            'work_id': work.id,
            'work_title': work.title,
            'work_description': work.description,
            'work_project_type': work.project_type,
            'work_repo_link': work.repo_link,
            'work_live_demo': work.live_demo,
            'work_thumbnail': str(work.thumbnail),
            'work_video': str(work.video),
            'work_tech': work.tech,
        }, status=status.HTTP_201_CREATED)

class WorkListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        queryset = Work.objects.all()
        if queryset.exists():
            serializer = WorkSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'No project found'},status=status.HTTP_404_NOT_FOUND)


class WorkDetailView(generics.RetrieveAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [AllowAny]
    lookup_field = "id"
    
class WorkUpdateView(generics.UpdateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [IsAdminUser]
    lookup_field = "id"
    
    def update(self, request, *args, **kwargs):
        work = self.get_object()

        serializer = self.get_serializer(work, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'message': "Project has been Updated",
            'work_id': work.id,
            'work_title': work.title,
            'work_decription': work.description,
            'work_project_type': work.project_type,
            'work_repo_link': work.repo_link,
            'work_live_demo': work.live_demo,
            'work_thumbnail': str(work.thumbnail),
            'work_video':str(work.video),
            'work_tech':work.tech
        }, status=status.HTTP_200_OK)

class WorkDeleteView(generics.DestroyAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [IsAdminUser]
    lookup_field = "id"
    
    def delete(self, request, *args, **kwargs):
        work = self.get_object()
        work.delete()
        return Response({'message': "Project has been Deleted"}, status=status.HTTP_200_OK)