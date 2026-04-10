from rest_framework import serializers
from work.models import Work

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'
        read_only_fields = ['owner']
        
        
    def create(self, validated_data):
        owner = validated_data.pop('owner', [])
        work = Work.objects.create(**validated_data)
        work.owner.set(owner)
        work.save()
        return work