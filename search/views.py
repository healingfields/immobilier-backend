from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from search.documents import ImmobilierDocument
from immobilier.serializers import ImmobilierSerializer
from django_elasticsearch_dsl_drf.pagination import LimitOffsetPagination

from django_elasticsearch_dsl_drf.filter_backends import (
    SearchFilterBackend,
    FilteringFilterBackend,
    SuggesterFilterBackend,
    CompoundSearchFilterBackend,
)


class ImmobilierDocumentView(DocumentViewSet):
    document = ImmobilierDocument
    serializer_class = ImmobilierSerializer
    pagination_class = LimitOffsetPagination
    lookup_field = "id"

    filter_backends = [
        SearchFilterBackend,
        FilteringFilterBackend,
    ]

    search_fields = ("city", "title")

    filter_fields = {"city": "city.raw", "title": "title.raw"}

    # ?city__terms=agadir__berrechid (filters with the exact terms)
