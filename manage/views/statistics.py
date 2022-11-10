from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from manage.filter import StatisticsTimeFilter
from manage.models.stats import Statistics
from manage.permissions import IsStatisticManager
from manage.serializers.statistics import ManageStatisticsSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ManageStatisticsDetail(generics.RetrieveAPIView):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StatisticsTimeFilter
    # permission_classes = (permissions.IsAuthenticated, IsStatisticManager)

    def get_queryparams(self):
        return self.request.query_params

    def get_object(self):
        query_params = self.get_queryparams()

        obj = Statistics(
            created_at=query_params.get('created_at'),
            start_at=query_params.get('start_at'),
            end_at=query_params.get('end_at')
        )
        self.check_object_permissions(self.request, obj)
        return obj

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ManageStatisticsSerializer(instance, context=self.get_serializer_context())
        return Response(serializer.data)
