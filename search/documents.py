from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from immobilier.models import Immobilier


@registry.register_document
class ImmobilierDocument(Document):
    class Index:
        name = "immobilier"

    class Django:
        model = Immobilier

        fields = [
            "id",
            "title",
            "type",
            "transaction",
            "city",
            "thumbnail_url",
            "posted_at",
        ]
