from django.db import models

# Create your models here.
class Immobilier(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    type = models.CharField(max_length=150, blank=True)
    transaction = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=150, blank=True)
    thumbnail_url = models.ImageField()
    postted_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.type} en {self.transaction} a {self.city}"
