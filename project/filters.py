import django_filters

from project.models import Project


class ProjectFilter(django_filters.FilterSet):
    date_created = django_filters.RangeFilter()

    class Meta:
        model = Project
        fields = ['status', 'date_created']
