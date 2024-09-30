from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.permissions import IsUser, IsLibrarian
from users.serializers import (UserCreateUpdateSerializer,
                               UserDetailsSerializer, UserSerializer)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUser, )

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailsSerializer
        if self.action in ["create", "update"]:
            return UserCreateUpdateSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (AllowAny,)
        elif self.action == "list":
            self.permission_classes = (IsLibrarian, )
        elif self.action in ["retrieve", "update", "destroy", "partial_update"]:
            self.permission_classes = (IsLibrarian | IsUser, )
        return super().get_permissions()



    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()
