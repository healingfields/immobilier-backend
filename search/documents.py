from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry


from immobilier.models import Immobilier


@registry.register_document
class ImmobilierDocument(Document):

    title = fields.TextField(
        attr="title",
        fields={"raw": fields.TextField()},
    )
    type = fields.TextField(
        attr="type",
        fields={"raw": fields.TextField()},
    )
    transaction = fields.TextField(
        attr="transaction",
        fields={"raw": fields.TextField()},
    )
    city = fields.TextField(
        attr="city",
        fields={"raw": fields.TextField()},
    )
    price = fields.TextField(
        attr="price",
        fields={"raw": fields.TextField()},
    )
    thumbnail_url = fields.FileField(attr="thumbnail_url")
    url = fields.TextField(
        attr="url",
        fields={"raw": fields.TextField()},
    )
    created_at = fields.DateField(
        attr="created_at",
        fields={"raw": fields.DateField()},
    )

    class Index:
        name = "immobiliers"

    class Django:
        model = Immobilier
