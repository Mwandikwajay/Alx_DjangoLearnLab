from rest_framework import serializers
from rest_framework.authtoken.models import Token  # For token creation
from django.contrib.auth import get_user_model  # To fetch the custom user model

User = get_user_model()

# User Registration Serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True)  # To return the token in response

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'bio', 'token']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create user using the built-in create_user method
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            bio=validated_data.get('bio', "")
        )

        # Generate a token for the user
        token, _ = Token.objects.get_or_create(user=user)

        # Attach the token to the serializer response
        user.token = token.key
        return user


# User Login Serializer
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
