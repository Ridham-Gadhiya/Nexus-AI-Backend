from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import Achievement
from rest_framework.response import Response
from .serializers import AchievementSerializer
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response


class AchievementCreateView(generics.CreateAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [IsAdminUser]
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        achievement = serializer.save(created_by = request.user)
        
        return Response({
            "achievement_id": achievement.id,
            "achievement_title": achievement.title,
            "achievement_description":achievement.description
        }, status=status.HTTP_201_CREATED)

class AchievementListView(generics.ListAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [AllowAny]
    
class AchievementUpdateView(generics.UpdateAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [IsAdminUser]
    lookup_field = "id"
    
    def update(self, request, *args, **kwargs):
        achievement = self.get_object()

        serializer = self.get_serializer(achievement, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'message': "Project has been Updated",
            'achievement_id': achievement.id,
            'achievement_title': achievement.title,
            'achievement_decription': achievement.description,
            'achievement_image': achievement.image,
            'achievement_image_link': str(achievement.img_link)
        }, status=status.HTTP_200_OK)

class WorkDeleteView(generics.DestroyAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [IsAdminUser]
    lookup_field = "id"
    
    def delete(self, request, *args, **kwargs):
        achievement = self.get_object()
        achievement.delete()
        return Response({'message': "Achievement has been Deleted"}, status=status.HTTP_200_OK)