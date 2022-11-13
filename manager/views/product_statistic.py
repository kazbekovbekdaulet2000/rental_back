from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions
from manager.models.statistics.product_statistic import ManagerProductStat
from manager.permissions import IsStatisticManager
from manager.serializers.product_statistic import ManagerProductStatSerializer


class ManagerStatisticProducts(generics.ListAPIView):
    serializer_class = ManagerProductStatSerializer
    # permission_classes = (permissions.IsAuthenticated, IsStatisticManager)
    product_stat = None
    pagination_class = None

    def get_queryparams(self):
        return self.request.query_params

    def get_queryset(self):
        params = self.request.query_params
        self.product_stat = ManagerProductStat(start_at=params.get('start_at'), end_at=params.get('end_at'))
        return self.product_stat
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=False)
        return Response(serializer.data)