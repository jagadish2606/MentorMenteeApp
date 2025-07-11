from rest_framework import serializers
from .models import Users
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        
        


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = Users
        fields = ['email', 'firstname', 'lastname', 'usertype', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        hashed_password = make_password(password)
        user = Users.objects.create(passwordhash=hashed_password, **validated_data)
        return user
    
    
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data['email']
        password = data['password']

        try:
            user = Users.objects.get(email=email)
        except Users.DoesNotExist:
            raise serializers.ValidationError({"error": "Invalid email or password"})

        if not check_password(password, user.passwordhash):
            raise serializers.ValidationError({"error": "Invalid email or password"})

        if not user.isactive:
            raise serializers.ValidationError({"error": "Account is inactive"})

        return {
            "user": user
        }