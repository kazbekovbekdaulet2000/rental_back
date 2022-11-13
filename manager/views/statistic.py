from rest_framework import generics
from rest_framework import permissions
from manager.models.statistics.statistic import ManagerStat
from manager.permissions import IsStatisticManager
from manager.serializers.statistic import ManagerStatSerializer


class ManagerStatistics(generics.RetrieveAPIView):
    serializer_class = ManagerStatSerializer
    # permission_classes = (permissions.IsAuthenticated, IsStatisticManager)
    stat = None

    def get_object(self):
        params = self.request.query_params
        self.stat = ManagerStat(start_at=params.get('start_at'), end_at=params.get('end_at'))
        return self.stat