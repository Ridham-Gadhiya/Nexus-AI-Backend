from rest_framework import serializers
from owner.models import User

class OwnerRegistraionSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    
    class Meta:
        model = User
        fields = ['id', 'name', 'surname', 'email', 'password', 'bio', 'contact_no']
        
    def create(self, validated_data):
        name = validated_data['name']
        surname = validated_data['surname']
        email = validated_data['email']
        password = validated_data['password']
        bio = validated_data['bio']
        user = User.objects.create_user(
            name=name,
            surname=surname,
            email=email,
            bio=bio,
        )
        user.set_password(password)
        user.save()
        return user

class ChangepasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    old_password = serializers.CharField(write_only=True, min_length=8)
    new_password = serializers.CharField(write_only=True, min_length=8)
    
# class ForgotPasswordSerializer(serializers.Serializer):
#     email = serializers.EmailField(required=True)

# class ResetPasswordSerializer(serializers.Serializer):
#     email = serializers.EmailField(required=True)
#     password = serializers.CharField(write_only=True, min_length=8)
#     confirm_password = serializers.CharField(write_only=True, min_length=8)