from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import Developer
from .serializers import DeveloperSerializer

class DeveloperCreateView(generics.CreateAPIView):
    serializer_class = DeveloperSerializer
    permission_classes = [IsAdminUser]
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.data)
        serializer.is_valid(raise_exception=True)
        developer = serializer.save()
        return Response({
            'message': "Developer profile created successfully",
            "developer_id": developer.id,
            "name":developer.name,
            "email": developer.email,
            "bio": developer.bio,
            "role": developer.role,
            "thumbnail": str(developer.thumbnail),
            "Linkedln": developer.linkedln,
            "Github": developer.github,
        }, status=status.HTTP_201_CREATED)

class DeveloperListView(generics.ListAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    permission_classes = [AllowAny]
    
class DeveloperUpdateView(generics.UpdateAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    permission_classes = [IsAdminUser]
    lookup_field = "id"
    
    def update(self, request, *args, **kwargs):
        developer = self.get_object()

        serializer = self.get_serializer(developer, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'message': "Project has been Updated",
            'developer_id': developer.id,
            'developer_name': developer.name,
            'developer_email': developer.email,
            'developer.bio': developer.bio,
            'developer.role': developer.role,
            'developer_thumbnail': str(developer.thumbnail),
            'developer_linkedln':str(developer.linkedln),
            'developer_github':developer.github
        }, status=status.HTTP_200_OK)

class DeveloperDeleteView(generics.DestroyAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    permission_classes = [IsAdminUser]
    lookup_field = "id"
    
    def delete(self, request, *args, **kwargs):
        developer = self.get_object()
        developer.delete()
        return Response({'message': "Project has been Deleted"}, status=status.HTTP_200_OK)
