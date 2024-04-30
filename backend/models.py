from django.db import models
from uuid import uuid4

class ContactUsModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    name = models.CharField(max_length=512, blank=True)
    email = models.EmailField(max_length=512, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=512, blank=True, null=True)
    service = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.company}) -- {self.service}"

class NewsLetterModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    email = models.EmailField(max_length=512, unique=True)