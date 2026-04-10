from rest_framework import serializers
from .models import About, Skill

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"
        
    def create(self, validated_data):
        about = About.objects.create(**validated_data)
        about.save()
        return about
        
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'category', 'icon']
        
    def create(self, validated_data):
        skill = Skill.objects.create(**validated_data)
        skill.save()
        return skill