from django_filters import rest_framework as filters
from manage.models.stats import Statistics


class StatisticsTimeFilter(filters.FilterSet):
    class Meta:
        model = Statistics
        fields = ['start_at', 'end_at']