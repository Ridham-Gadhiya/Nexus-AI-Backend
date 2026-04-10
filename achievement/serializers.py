from rest_framework import serializers
from .models import Achievement

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ['id', 'title', 'description', 'image', 'img_link']
        
    def create(self, validated_data):
        achievement = Achievement.objects.create(**validated_data)
        achievement.save()
        return achievement
        