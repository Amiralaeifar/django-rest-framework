from rest_framework import serializers
from django.contrib.auth.models import User



def clean_email(value):
    user = User.objects.filter(email=value).exists()
    if user:
        raise serializers.ValidationError('there is an account with this email, please enter a new one')
    return value


class UserRegisterSeralizer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, write_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'validators': [clean_email,]},
        }
    
    
    def create(self, validated_data):
        del validated_data['password2']
        return User.objects.create_user(**validated_data)
    
    
    def update(self, instance, validated_data):
        del validated_data['password2']
        return User.objects.filter(username=instance.username).update(**validated_data)
    
    
    def validate_username(self, value):
        user = User.objects.filter(username=value).exists()
        if user:
            raise serializers.ValidationError('username must be unique')
        return value
    
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('password must match')
        return data
    
    
    
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
        
        