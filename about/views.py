from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import About, Skill
from rest_framework.response import Response
from .serializers import AboutSerializer, SkillSerializer


class AboutCreateView(generics.CreateAPIView):
    serializer_class = AboutSerializer
    permission_classes = [IsAdminUser]
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        about = serializer.save()
        
        return Response({
            'message': 'About information has been created',
            'about_id': about.id,
            'about_bio': about.bio,
            'about_profile_picture': str(about.profile_picture),
        }, status=status.HTTP_201_CREATED)

class AboutInfoView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [AllowAny]
    
class SkillCreateView(generics.CreateAPIView):
    serializer_class = SkillSerializer
    permission_classes = [IsAdminUser]
    
    def post(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            skill = serializer.save()
            
            return Response({
                'message': 'Skill has been created',
                'skill_id': skill.id,
                'name': skill.name,
                'icon': str(skill.icon),
            }, status=status.HTTP_201_CREATED)

class SkillListView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [AllowAny]
    
class AboutUpdateView(generics.UpdateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [IsAdminUser]
    lookup_field = "id"
    
    def update(self, request, *args, **kwargs):
        about = self.get_object()

        serializer = self.get_serializer(about, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'message': "Project has been Updated",
            'about_id': about.id,
            'name': about.name,
            'about_decrtaglineiption': about.tagline,
            'about_description': about.description,
            'about_logo': str(about.logo),
            'about_established_year': about.established_year,
            'about_linkedln': about.linkedln,
            'about_twitter':about.twitter,
            'about_github':about.github
        }, status=status.HTTP_200_OK)
        
class SkillUpdateView(generics.UpdateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAdminUser]
    lookup_field = "id"
    
    def update(self, request, *args, **kwargs):
        skill = self.get_object()

        serializer = self.get_serializer(skill, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'message': "Project has been Updated",
            'skill_id': skill.id,
            'skill_name': skill.name,
            'skill_decrtaglineiption': skill.category,
            'skill_logo': str(skill.icon),
        }, status=status.HTTP_200_OK)