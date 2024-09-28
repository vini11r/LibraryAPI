from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import (UserCreateUpdateSerializer,
                               UserDetailsSerializer, UserSerializer)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailsSerializer
        if self.action in ["create", "update"]:
            return UserCreateUpdateSerializer
        return UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()
