from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model  # Import get_user_model

# Get the custom user model
User = get_user_model()

# User Registration Serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True)  # Include the token in the response

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'bio', 'token']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Explicitly create the user
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            bio=validated_data.get('bio', "")
        )

        # Explicitly create a token for the user
        token = Token.objects.create(user=user)

        # Add the token to the user response
        user.token = token.key
        return user


# User Login Serializer
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
