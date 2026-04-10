from rest_framework import serializers
from .models import Developer

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = ['id', 'name', 'email', 'bio', 'role', 'thumbnail', 'linkedln', 'github']
        
    def create(self, validated_data):
        developer = Developer.objects.create(**validated_data)
        developer.save()
        return developer