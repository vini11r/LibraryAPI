from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserSerializer, UserDetailsSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailsSerializer
        return UserSerializer
