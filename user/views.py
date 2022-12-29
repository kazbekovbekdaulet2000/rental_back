from rest_framework import generics, permissions
from user.serializers import ProfileSerializer


class ProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_object(self):
        obj = self.request.user
        self.check_object_permissions(self.request, obj)
        return obj
