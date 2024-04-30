from rest_framework import serializers

from backend.models import ContactUsModel, NewsLetterModel

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsModel
        fields = "__all__"

class NewsLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLetterModel
        fields = "__all__"