from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from manager.permissions import IsStatisticManager
from manager.serializers.rentinhand import ManagerRentInHandSerializer


class ManagerRentInHandFile(generics.CreateAPIView):
    serializer_class = ManagerRentInHandSerializer
    permission_classes = (permissions.IsAuthenticated, IsStatisticManager)
    parser_classes = [MultiPartParser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_201_CREATED, headers=headers)
