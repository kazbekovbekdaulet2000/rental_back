from rest_framework import generics
from rest_framework import permissions
from manage.models.stats_product import ProductStatistics
from manage.permissions import IsStatisticManager
from manage.serializers.product_statistics import ManagerProductStatisticsSerializer


class ManageStatisticProducts(generics.ListAPIView):
    serializer_class = ManagerProductStatisticsSerializer
    # permission_classes = (permissions.IsAuthenticated, IsStatisticManager)
    product_stat = None
    pagination_class = None

    def get_queryparams(self):
        return self.request.query_params

    def get_queryset(self):
        params = self.request.query_params
        self.product_stat = ProductStatistics(start_at=params.get('start_at'), end_at=params.get('end_at'))
        return self.product_stat.product_count
        