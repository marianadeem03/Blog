from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User
from users.api.serializers import UserSerializers, UserRegistrationSerializer, UserLoginSerializer


# Create your views here.
class ListUsers(APIView):
    """
    View to list all users in the system.
    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, format = None):
        """
        Return a list of all users.
        """
        # email = [User.email for User in User.objects.all()]
        all_users = User.objects.all()
        serializer = UserSerializers(all_users, many=True)
        print(all_users)
        return Response(serializer.data)


# Generating Tokens manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
    }


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response("User successfully registered", status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    def post(self, request, format = None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                user_type = user.get_role_types_display()
                token = get_tokens_for_user(user)
                return Response({'token': token, 'role': user_type}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid credentials"}, status=status.HTTP_404_NOT_FOUND)
