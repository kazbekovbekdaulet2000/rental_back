from rest_framework import generics
from manager.models.constants import ManagerContants
from manager.serializers.constants import ManagerContantsSerializer
from rest_framework import permissions


class ConstantsView(generics.RetrieveAPIView):
    lookup_field = None
    queryset = None
    serializer_class = ManagerContantsSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_object(self):
        obj = ManagerContants()
        self.check_object_permissions(self.request, obj)
        return obj
